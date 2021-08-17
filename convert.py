import configparser
import glob
import os


CONFIG_PATH = 'config.ini'


def read_config(config_path:str)->configparser.ConfigParser:
    """Return config

    """
    config = configparser.ConfigParser()
    config.read(config_path)

    assert 'DEFAULT' in config
    assert 'IconPath' in config['DEFAULT']
    
    return config

def convert(path:str)->None:
    """Recursively iterate the folder tree and convert biggest png files

    folder tree structure for material icons;
    - ROOT
      - category
        - icon name
          - materialiconsoutlined
          - materialiconstwotone
          - materialiconssharp
          - materialiconsround
          - materialicons
            - 18dp
            - 24dp
            - 36dp
            - 48dp
              - 1x
              - 2x
              - 3x
              - 4x
    """
    type_priority = ['materialicons',
                     'materialiconssharp',
                     'materialiconsround', 
                     'materialiconstwotone', 
                     'materialiconsoutlined' ]
    size_priority = ['48dp', '36dp', '24dp', '18dp']
    zoom_priority = ['4x', '3x', '2x', '1x']

    folders = glob.glob(path+'/**/**')

    for f in folders:
        types = glob.glob(f+'/*')
        types = [path.replace(f+'/', '') for path in types]

        picked_priority = None
        for _type in type_priority:
            if _type in types:
                picked_priority = _type
                break
        
        assert picked_priority is not None

        f = f + '/' + picked_priority

        sizes = glob.glob(f+'/*')
        sizes = [path.replace(f+'/', '') for path in sizes]

        picked_size = None
        for _size in size_priority:
            if _size in sizes:
                picked_size = _size
                break
        
        assert picked_size is not None

        f = f + '/' + picked_size
        print(f)



    return


def main(*args:list, **kargs:dict)->None:
    config = read_config(CONFIG_PATH)
    icon_path = config['DEFAULT']['IconPath']

    convert(icon_path)	
    
    return

if __name__ == '__main__':
    main()