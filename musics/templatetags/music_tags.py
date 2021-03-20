from django import template
import math

register=template.Library()

@register.filter
def time_formater(time):
    print(type(time))
    time=int(time)
    min=math.floor((time%3600)/60)
    sec=math.floor(time%60)
    
    if (sec<10):
      sec=f"0{sec}"
      
    return f"{min}:{sec}"
    