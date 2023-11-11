"""Add title and subtitles to a Matplotlib figure in a neat and easy way.
"""
import matplotlib

def set_title_and_subtitle(fig:matplotlib.figure.Figure, 
                           title:str, 
                           subtitle:str, 
                           alignment:str='left', 
                           title_size:float=16, 
                           subtitle_size:float=13, 
                           v_space:float=2,
                           h_offset:float=2, 
                           v_offset:float=2):
    """Add title and subtitle to a Matplotlib figure. Placement is based
    on figure coordinates.
    
    Args:
        fig:
            Handle to the Matplotlib figure.
        title: 
            The title.        
        subtitle: 
            The subtitle.
        alignment: 
            The horizontal alignment. Possible values are 'left', 
            'center' or 'right'.
        title_size: 
            The title font size (in pt). 
        subtitle_size:
            The subtitle font size (in pt).
        v_space: 
            Vertical space between title and subtitle (in pt).
        h_offset:
            Horizontal offset (in pt). A positive (negative) value 
            specifies the amount of horizontal displacement towards the 
            right (left) of the figure. The reference (zero) is the text 
            anchor point as specified by 'aligment'.
        v_offset:
            Vertical offset (in pt). A positive value specifies the 
            amount of vertical displacement towards the bottom of the 
            figure starting from the top border. A negative value has no 
            effect.

    Returns: 
        None.
        
    Examples:
        >>> import matplotlib.pyplot as plt
        >>> fig, ax = plt.subplots(figsize=(5,6))
        >>> set_title_and_subtitle(fig=fig, title='Figure title', 
        ...                        subtitle='Figure subtitle')
        >>> fig.savefig(fname='title1.png')

"""

    PT_TO_IN = 1/72   #Points to inches conversion factor
    
    #Get the figure size
    width, height = fig.get_size_inches()
        
    #Vertical space in figure coordinates
    v_space = v_space*PT_TO_IN/height
    
    #Vertical position in figure coordinates
    v_offset = v_offset*PT_TO_IN if v_offset >= 0 else 0
    v_pos = 1.0 - v_offset/height
    
    h_offset = h_offset*PT_TO_IN/width
    if alignment == 'left':
        title_loc = (h_offset, v_pos)
    elif alignment == 'center':
        title_loc = (0.5 + h_offset, v_pos)
    elif alignment == 'right':
        title_loc = (1.0 - h_offset, v_pos)
    else:
        raise Exception(f'Alignment *{alignment}* not supported')
    
    #Subtitle is horizontally aligned with title and shifted dowwards
    #by v_space
    subtitle_loc = (title_loc[0], 
                    title_loc[1] - v_space - title_size*PT_TO_IN/height)
    
    text_kwds = {'horizontalalignment': alignment,
                 'verticalalignment':'top'}
    
    fig.text(*title_loc, title, fontweight="bold", fontsize=title_size, 
             transform=fig.transFigure, **text_kwds)
    fig.text(*subtitle_loc, subtitle, fontsize=subtitle_size, 
             transform=fig.transFigure, **text_kwds)    