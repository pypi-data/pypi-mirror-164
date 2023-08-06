# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ Copyright 2022. quinn.7@foxmail.com All rights reserved.                 ║
# ║                                                                          ║
# ║ Licensed under the Apache License, Version 2.0 (the "License");          ║
# ║ you may not use this file except in compliance with the License.         ║
# ║ You may obtain a copy of the License at                                  ║
# ║                                                                          ║
# ║ http://www.apache.org/licenses/LICENSE-2.0                               ║
# ║                                                                          ║
# ║ Unless required by applicable law or agreed to in writing, software      ║
# ║ distributed under the License is distributed on an "AS IS" BASIS,        ║
# ║ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ║
# ║ See the License for the specific language governing permissions and      ║
# ║ limitations under the License.                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
"""
@ 模块     : 命令行指令通用模块   
@ 作者     : chenjiancheng
@ 邮箱     : quinn.7@foxmail.com
@ 编写时间 : 2022-08-10

@ 模块描述 :
    NULL

"""
from ..baseic.const import CONST
from ..baseic.message_recorder import window_template_output


NUMBER_NESTING_LAYERS = 3
""" 工程目录嵌套最大层数 """


def confirm_root_directory_runtime_project():
    """
    [ 确认运行时工程的根目录 ]

    ---
    描述:
        NULL

    """
    cwd = CONST.Path.CWD

    for _ in range(NUMBER_NESTING_LAYERS):
        engineering_init = cwd.joinpath(CONST.Name.FileName.EngineeringInit)
        if engineering_init.exists():
            CONST.Path.CWD = cwd
            CONST.Path.DirPath.Data = cwd.joinpath(CONST.Name.DirName.EngineeringData)
            CONST.Path.DirPath.Logs = CONST.Path.DirPath.Data.joinpath(CONST.Name.DirName.EngineeringLogs)
            CONST.Path.DirPath.BaseCode = CONST.Path.DirPath.Data.joinpath(CONST.Name.DirName.EngineeringBaseCode)
            CONST.Path.FilePath.Init = cwd.joinpath(CONST.Name.FileName.EngineeringInit)
            CONST.Path.FilePath.Config = CONST.Path.DirPath.Data.joinpath(CONST.Name.FileName.EngineeringConfig)
            CONST.Path.FilePath.Database = CONST.Path.DirPath.Data.joinpath(CONST.Name.FileName.EngineeringDatabase)
            return True
        else:
            cwd = cwd.resolve().parent
            continue
    
    window_template_output(
        [
            '- 检查环境 -',
            None,
            '当前运行路径不是Awaken工程结构路径;',
            '请在工程根目录中执行工程初始化命令:',
            None,
            'awaken -init'
        ],
        clean=False
    )
    exit(0)
