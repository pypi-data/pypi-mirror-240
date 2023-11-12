
import dash_mantine_components as dmc

# local
from .layout_utils import (
    comp_id,
    placeholder_text,
    BORDER_COLOR,
    PAPER_BCOLOR,
    )

# Body left is the layout of the main body left column
# Contains and controls the search input, search radio, member tabs, and 
# member lists        
body_left = dmc.Card([
    dmc.CardSection(
        dmc.TextInput(
            placeholder='Search Current Members',
            type='text',
            size='sm',
            id=comp_id('search-input', 'search', 0),
        ),
        style={
            'height':'2.5em',
            'width':'100%',
            'margin':'0',
            'padding':'4px 10px 2px 10px',
        }
    ),
    dmc.CardSection(
        dmc.RadioGroup([
            dmc.Radio('Starts With', value='startswith'),
            dmc.Radio('Contains', value='contains'),
            ],
            value='startswith',
            orientation='horizontal',
            size='sm',
            spacing='xs',
            id=comp_id('search-radio', 'search', 0),
        ),
        style={
            'height':'2.5em',
            'width':'100%',
            'margin':'auto',
            'padding':'0 0 2px 10px',
        }
    ),
    dmc.CardSection(
        dmc.Tabs([
            dmc.TabsList(
                children=[],
                id=comp_id('m-tabs', 'tabs', 0),
                grow=True,
            ),
            ],
            id=comp_id('m-tabs-group', 'tabs', 0),
            value='modules',
            variant='default',
            color='blue',
            orientation='horizontal',
        ),
        style={
            'width':'100%',
            'margin':'0',
            'padding':'4px 0 0 0',
        }
    ),
    dmc.CardSection(
        placeholder_text('Explorer Members'),
        id=comp_id('m-tabs-content', 'tabs', 0),
        style={
            'height':r'calc(100% - 11em - 8px)',
            'max-height':r'calc(100% - 11em - 8px)',
            'width':'100%',
            'margin':'4px 0 0 0',
            'padding':'4px 4px 4px 10px',
            'overflow':'auto',
        }
    ),
    dmc.Group([
        dmc.Text(
            'Include Private Members ',
            italic=True,
            color='#5a5a5a',
            style={
                'font-size':'0.8em',
                'font-weight':'400',
                'padding':'0 0 2px 0',
            }
        ),
        dmc.Switch(
            id=comp_id('private-switch', 'tabs', 0),
            size='sm',
            radius='lg',
            checked=False,
        ),
        ],
        position='center',
        spacing=4,
        noWrap=True,
        align='end',
        style={
            'position':'absolute',
            'bottom':'6px',
            'right':'6px',
        }
    ),
    ],
    radius=0,
    shadow='lg',
    style={
        'border-left':f'1px solid {BORDER_COLOR}',
        'border-bottom':f'1px solid {BORDER_COLOR}',
        'border-bottom-left-radius':'10px',
        'height':'100%',
        'width':'100%',
        'position':'relative',
        'margin':'0',
        'padding':'0',
        'background-color':PAPER_BCOLOR,
    }
),