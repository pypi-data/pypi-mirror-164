# Copyright 2022. quinn.7@foxmail.com All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""
[ WEB 执行器 ]

"""
import time
import asyncio

from playwright.async_api import async_playwright

from .web_engine import WebEngine
from ...baseic.log import LOG
from ...baseic.const import CONST
from ...baseic.config import CONFIG
from ...baseic.keyword import KEYWORD
from ...baseic.message_recorder import MESSAGE_RECORDER
from ...baseic.error import AwakenWebEngineRunError
from ...baseic.error import AwakenTaskPretreatmentError
from ...kit.global_method import GlobalMethod
from ...server.task_db_broker import TaskDbBroker
from ...core.interpreter.structural import AwakenTask
from ...core.interpreter.structural import AwakenCase
from ...core.interpreter.structural import AwakenCodeLine
from ...core.interpreter.common import converting_para_format


class WebRunner: ...


class WebRunner:
    """
    [ WEB 执行器 ]

    ---
    描述:
        NULL

    """
    _task: AwakenTask
    _global_method: GlobalMethod = GlobalMethod()
    _web_engine: WebEngine
    _use_case_in_execution: AwakenCase
    _task_db_broker: TaskDbBroker = None


    def __init__(self, task: AwakenTask) -> None:
        self._task = task

        if CONFIG.is_write_database:
            self._task_db_broker = TaskDbBroker(CONST.Type.Task.Web)


    def start(self, *_):
        """
        [ 开始任务 ]

        ---
        描述:
            NULL

        """
        return asyncio.run(self._async_running_task())


    async def _async_running_task(self):
        """
        [ 协程执行任务 ]

        ---
        描述:
            NULL

        """
        task_state = CONST.State.Result.Null

        try:
            async with async_playwright() as playwright:
                # 创建 playwright 对象
                self._web_engine = WebEngine()
                self._web_engine._init_playwright(playwright)

                # 数据库创建任务
                if self._task_db_broker:
                    self._task_db_broker.task_start(
                        str(self._task.namespace[KEYWORD.Script.Namespace.TaskName]),
                        str(self._task.namespace[KEYWORD.Script.Namespace.TaskDocs]),
                    )

                # 启动浏览器
                await self._web_engine._browser_start(self._task.namespace[KEYWORD.Script.Decorator.BrowserType])

                # 遍历任务的用例
                for awaken_case in self._task.test_cases.values():
                    self._use_case_in_execution = awaken_case

                    # 数据库创建用例
                    if self._task_db_broker:
                        case_id = self._task_db_broker.created_case(
                            str(self._use_case_in_execution.name),
                            str(self._use_case_in_execution.docs)
                        )

                    try:
                        case_state = CONST.State.Result.Null
                        case_run_step = ''
                        case_start_time = time.strftime("%H:%M:%S")
                        case_start_timestamp = int(time.time())

                        # 启动页面
                        await self._web_engine._page_start()

                        # 遍历用例的步骤
                        for awaken_codeline in self._use_case_in_execution.steps:

                            # 赋值逻辑
                            if awaken_codeline.type == CONST.Interpreter.CodeLineType.Give:
                                self._give_cases_assignment(
                                    awaken_codeline.give_region,
                                    awaken_codeline.give_name,
                                    awaken_codeline.give_value,
                                )

                            # 执行并赋值逻辑
                            elif awaken_codeline.type == CONST.Interpreter.CodeLineType.RGive:
                                result = await self._running_function(awaken_codeline)
                                self._give_cases_assignment(
                                    awaken_codeline.give_region,
                                    awaken_codeline.give_name,
                                    result,
                                )
                                
                            # 执行逻辑
                            elif awaken_codeline.type == CONST.Interpreter.CodeLineType.Run:
                                await self._running_function(awaken_codeline)

                            # 断言逻辑
                            elif awaken_codeline.type == CONST.Interpreter.CodeLineType.Assert:
                                assert_result = self.assert_logic(awaken_codeline.assert_value)

                                if assert_result == True:
                                    case_state = CONST.State.Result.Success
                                else:
                                    case_state = CONST.State.Result.Unsuccess

                    except BaseException as error:
                        case_state = CONST.State.Result.Error
                        case_run_step = str(error)
                        MESSAGE_RECORDER.record(str(error))

                    finally:
                        if self._task_db_broker:
                            self._task_db_broker.update_case(
                                case_id,
                                case_state,
                                case_start_time,
                                case_start_timestamp,
                                '',
                            )

                    time.sleep(1)
                    await self._web_engine._page_close()

                if self._task_db_broker:
                    self._task_db_broker.task_end(task_state)
                    
                await self._web_engine._exit()

        except BaseException as error:
            import traceback
            LOG.error(traceback.format_exc())
            MESSAGE_RECORDER.template_print()


    async def _running_function(self, codeline: AwakenCodeLine):
        try:
            function_map = None
            function_engine = None
            
            if codeline.funtion_region == CONST.Interpreter.CodeLineScopet.Local:
                function_map = self._task.engine_function_map
                function_engine = self._web_engine
            else:
                function_map = self._task.global_function_map
                function_engine = self._global_method
            
            if codeline.funtion_name not in function_map.keys():
                raise AwakenWebEngineRunError('不合法的方法 !')

            new_function_value = self.parsing_method_parameters(codeline.funtion_value)

            if codeline.funtion_region == CONST.Interpreter.CodeLineScopet.Global:
                result = function_map[codeline.funtion_name](function_engine, *new_function_value)
            else:
                result = await function_map[codeline.funtion_name](function_engine, *new_function_value)
            return result

        except KeyError:
            import traceback
            LOG.error(traceback.format_exc())
            LOG.info(f'方法集中不存在这样的方法 :: [{ codeline.funtion_name }] !')


    def _give_cases_assignment(self, give_region: str, give_name: str, give_value: str):
        """
        [ 私域赋值封装 ]

        """
        give_path_node = give_name.split(CONST.Interpreter.GrammarSymbol.Statement)
        give_path_node_number = len(give_path_node)
        current_node = None
        if give_region == CONST.Interpreter.CodeLineScopet.Local:
            current_node = self._use_case_in_execution.namespace
        else:
            current_node = self._task.namespace
        i = 1
        if give_path_node_number > 1:
            for node in give_path_node:
                if i == give_path_node_number:
                    current_node.update({node: give_value})
                else:
                    if node not in current_node.keys():
                        current_node.update({node: {}})
                    current_node = current_node[node]
                    i += 1
        else:
            current_node.update({give_name: give_value})


    def assert_logic(self, assert_value: list):
        condition_count = len(assert_value)
        assert_result = None

        if condition_count == 1:
            calculation_member = [assert_value[0]]
            assert_result = converting_para_format(self.parsing_method_parameters(calculation_member)[0])
            
        elif condition_count == 3:
            calculation_symbol = assert_value[1]
            calculation_lvalue = converting_para_format(self.parsing_method_parameters([assert_value[0]])[0])
            calculation_rvalue = converting_para_format(self.parsing_method_parameters([assert_value[2]])[0])

            try:
                if type(calculation_lvalue) != type(calculation_rvalue):
                    raise AwakenWebEngineRunError('断言异常 :: 参与断言的左值与右值类型不一致 !')

                if calculation_symbol == '==':
                    assert_result = calculation_lvalue == calculation_rvalue
                elif calculation_symbol == '>':
                    assert_result = calculation_lvalue > calculation_rvalue
                elif calculation_symbol == '>=':
                    assert_result = calculation_lvalue >= calculation_rvalue
                elif calculation_symbol == '<':
                    assert_result = calculation_lvalue < calculation_rvalue
                elif calculation_symbol == '<=':
                    assert_result = calculation_lvalue <= calculation_rvalue

            except BaseException:
                return False

        return assert_result == True


    def parsing_method_parameters(self, source_data: list):
        """
        [ 解析方法参数 ]

        """
        filter_data = []
        if len(source_data) > 0:
            for value in source_data:
                if isinstance(value, str):
                    value_quote_symbol_count = value[0:2].count(CONST.Interpreter.GrammarSymbol.Quote)
                    para = value[value_quote_symbol_count:]

                    if value_quote_symbol_count != 0:
                        current_node = self._task.namespace
                    else:
                        current_node = self._use_case_in_execution.namespace

                    para_statement_symbol_count = para.count(CONST.Interpreter.GrammarSymbol.VariablePath)
                    if para_statement_symbol_count != 0:
                        para_nodes = para.split(CONST.Interpreter.GrammarSymbol.VariablePath)

                        if len(para_nodes) > 1:
                            for node in para_nodes:
                                try:
                                    current_node = current_node[node]
                                except KeyError:
                                    AwakenTaskPretreatmentError(CONST.Error.Interpreter.GrammarNamespaceNodeNotExist('#NODE#', node))
                        else:
                            try:
                                current_node = current_node[para_nodes[0]]
                            except:
                                AwakenTaskPretreatmentError(CONST.Error.Interpreter.GrammarNamespaceNodeNotExist('#NODE#', node))

                        filter_data.append(current_node)

                    else:
                        # 如果 para 存在于私域命名空间中则取出, 否则视为普通字符串
                        if para in current_node.keys():
                            filter_data.append(current_node[para])
                        else:
                            filter_data.append(para)
                else:
                    filter_data.append(value)

        return filter_data
