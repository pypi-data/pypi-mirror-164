import sys
import os
import subprocess
import glob


def get_current_ctx_name():
    ctx_name = get_env('CC_NAME').rstrip()
    return ctx_name

def get_current_ctx_id():
    return  get_env('CC_ID').rstrip()

def read_ctx_file(path):
    lines = []
    with open(path) as f:
        lines = f.readlines()

    ctx = {}
    for line in lines:
        key, val = line.rstrip().split(sep=',')
        ctx[key] = val
    return ctx

def load_config(match_pattern='.'):
    cfg = {}

    if match_pattern == '.':
        ctx_name = get_current_ctx_name()
        path = os.path.join(os.environ['CC_CFG_HOME'], "cc." + ctx_name.rstrip() + ".dat")
        paths = [path]
    elif match_pattern == '*':
        pattern = os.path.join(os.environ['CC_CFG_HOME'], "cc.*.dat")
        paths = glob.glob(pattern)
    
    for path in paths:
        try:
            ctx = read_ctx_file(path)
        except FileNotFoundError:
            print("no context")
            exit()
        id = ctx['CC_ID']
        cfg[id] = ctx
    return cfg

def set_env(key, val):
    os.environ[key] = val
    os.putenv(key, val)
    subprocess.call(['set', key, val], shell=True)

def get_env(key):
    return os.environ.get(key, 'none')

def switch_context(ctx_name):
      cfg = load_config()
      ids  = [ k  for k in list(cfg.keys())]
      names = [cfg[k]['CC_NAME'] for k in ids]
      name_to_id = dict(zip(names, ids))

      print('---------------------------')
      ctx_keys = list(cfg[name_to_id[ctx_name]].keys())

      for key in ctx_keys:
          id = name_to_id[ctx_name]
          val = cfg[id][key]
          set_env(key, val)
          if key in ['CC_SCRIPT']:
            subprocess.call([os.environ['CC_SCRIPT']])

      print('---------------------------')
      print('switched to', get_env('CC_NAME'))
       
def show_context():
      ctx_name = get_current_ctx_name()
      print("contex: ", ctx_name)

def show_help(program):
      print(program + "      : show current context")
      print(program + " <ctx>: switch to context")
      print(program + " info : show current context variables")
      print(program + " help : show this help")
  
def show_info():
      print('context list:')
      cfgs = load_config('*')
      print('---------------------------')
      ids  = [ k  for k in list(cfgs.keys())]
      names = [cfgs[id]['CC_NAME'] for id in ids]

      for id, key in zip(ids, names):
          print(id, key)
      print('---------------------------')
       
      cfg = load_config('.')
      ctx_name = get_current_ctx_name()
      id = get_current_ctx_id()
      ctx_keys = list(cfg[id].keys())

      ids  = [ k  for k in list(cfg.keys())]
      names = [cfg[k]['CC_NAME'] for k in ids]
      name_to_id = dict(zip(names, ids))

      print('')
      print('current context: ', ctx_name)
      print('---------------------------')
      for key in ctx_keys:
          id = name_to_id[ctx_name]
          val = cfg[id][key]
          print(key, val)
      print('---------------------------')
      

def handle_set_cmd(cfg, name_to_id, key, val):
    ctx_name = get_current_ctx_name()
    set_env(key, val)
    cfg[name_to_id[ctx_name]] = val

  
def main():
  commands = ['info', 'set', 'help']
  
  if len(sys.argv) == 1:
      show_context()
  elif (sys.argv[1] in commands):
      cmd = sys.argv[1]
      if cmd == 'help':
          show_help('cc.')
      elif cmd == 'info':
          show_info()
      elif cmd == 'set':
          handle_set_cmd(cfg, name_to_id, sys.argv[2], sys.argv[3]) 
  elif len(sys.argv) == 2:
      cfg = load_config('.')
      ids  = [ k  for k in list(cfg.keys())]
      names = [cfg[k]['CC_NAME'] for k in ids]
      if sys.argv[1] in names:
          ctx = sys.argv[1]
          switch_context(ctx)
      
  else:
      print('error: unknown context')
 
if __name__ == "__main__":
    main()
