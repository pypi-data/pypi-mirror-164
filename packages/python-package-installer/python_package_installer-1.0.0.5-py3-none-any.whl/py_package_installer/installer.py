from importlib_metadata import version as check_version
from importlib_metadata import PackageNotFoundError
from subprocess import CalledProcessError, check_call
from sys import executable

class installer:
    
    __command_line = {
        "python": executable, 
        "command": "-m pip install", 
        "package": "", 
        "upgrade": ""
    }
    
    __git_info = {
        "git": "", 
        "token": ""
    }
    
    __no_print = False
    
    def __init__(self, package_name:str, **kwargs):
        """
        function: python package install in pypi
        
        if package is in git only, try installer(package_name).git()
        
        Parameter
        --------
        (essential)
        - package_name: str
        
        (optional)
        - no_print: bool; default=False
        """
        
        if "no_print" in kwargs: no_print = kwargs["no_print"]
        else: no_print = self.__no_print
        
        self.pkg_name = package_name
        
        try:
            self.prev_version = check_version(package_name)
            self.action = "upgrade"
            
        except PackageNotFoundError:
            self.action = "install"
            
        finally:
            if self.action == "upgrade": self.__command_line.update({"upgrade": "--upgrade"})
            self.command_line = self.__complete_cmd_line("pypi")
            
            self.__run()
            
            if not no_print: print(self.result_txt)
            
    def git(self, **kwargs):
        """
        function: python package install using git url, token
        
        Parameter
        --------
        (essential)
        - git_url: str
        
        (optional)
        - no_print: bool; default=False
        - token: str
        """
        
        if "no_print" in kwargs: no_print = kwargs["no_print"]
        else: no_print = self.__no_print
        
        self.__git_info.update({key: value for key, value in kwargs.items() if key in self.__git_info})
        
        if self.__git_info["git"] == "":
            print("need git url")
        else:
            self.command_line = self.__complete_cmd_line("git", **self.__git_info)
            self.__run()
            if not no_print: print(self.result_txt)
            
    def __run(self):
        try:
            self.__install_result = check_call(self.command_line)
            error = False
            
        except CalledProcessError:
            error = True
            
        finally:
            self.__install_result = self.__check_install_result(error, self.pkg_name)
    
    def __check_install_result(self, error:bool, package_name:str):
        
        result = 0
        
        if error:
            result = -1
        else:
            self.new_version = check_version(package_name)
            if (
                self.action == "upgrade" and 
                (self.prev_version == self.new_version)
            ): result = 1
            
        return result
    
    def __complete_cmd_line(self, cat:str, **kwargs):
        
        self.__cat = cat
        
        if self.__cat == "git":
            token = kwargs["token"]
            git = kwargs["git"]
            package = f"git+https://{token}@{git}"
        
        elif self.__cat == "pypi":
            package = self.pkg_name
            
        command_dict = self.__command_line.copy()
        command_dict.update({"package": package})
        
        result = " ".join([value for value in command_dict.values() if value != ""])
        
        return result
    
    @property
    def result_txt(self):
        
        linear = {
            "txt": "="*30, 
            "error1": "="*20, 
            "error2": "="*16
        }
        
        if self.__install_result == -1: # 에러발생
            if self.__cat == "pypi":
                linear = f"+{linear['error1']}+"
                comment = "package not found".center(len(linear)-2, " ")
                recommand = "please try installing by git"
                
            elif self.__cat == "git":
                linear = f"+{linear['error2']}+"
                comment = "error occurred".center(len(linear)-2, " ")
                recommand = "please contact administer"
                
            result = f"{linear}\n+{comment}+"
            
        else:
            linear = f"+{linear['txt']}+"
            comment = f"installed version: {self.new_version}".center(len(linear)-2, " ")
            result = f"{linear}\n+{comment}+"
            
            if self.__install_result == 0: # 설치/업그레이드 완료
                if self.action == "install":
                    recommand = "please load the package to use"
                
                elif self.action == "upgrade":
                    old_ver_txt = f"old version: {self.prev_version}".center(len(linear)-2, " ")
                    new_ver_txt = f"new version: {self.new_version}".center(len(linear)-2, " ")
                    
                    result = f"{linear}\n+{old_ver_txt}+"
                    result += f"\n+{new_ver_txt}+"
                    
                    recommand = "please reload the package to use new version"
            
                empty_space = " "*(len(linear)-2)
                result += f"\n+{empty_space}+"
                comment2 = f"package {self.action} complete".center(len(linear)-2, " ")
                result += f"\n+{comment2}+".center(len(linear), " ")
                
            elif self.__install_result == 1: # 업그레이드 존재 X
                recommand = f"no upgrade exist in {self.__cat}"
                
        result += f"\n{linear}\n\n{recommand.upper()}"
        
        return result
    