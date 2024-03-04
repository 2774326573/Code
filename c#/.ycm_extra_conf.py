import ycm_core
 
def PythonModuleCompletion( filename, line, column ):
  return [ 'os', 'sys' ]
 
def TranslateCSharpCode( code, filename ):
  # 这里可以添加代码来转换C#代码到YCM理解的形式
  return code
 
def Settings( **kwargs ):
  # 指定你的C#编译器路径，例如使用mcs
  return {
    'flags': [
      '-mcs',
      '--add-auto-reference=Imagesharp.dll',
      '--nowarn:1701,1702,2008',
      '--warnaserror=1685,1689',
      '--define:DEBUG',
      '--optimize-',
      '-unsafe+',
      '-sdk:4.5',
    ],
    'include_paths_relative_to_dir': 'CSharpProjectDir',
    'override_filename': lambda filename: filename + '.cs'
  }
