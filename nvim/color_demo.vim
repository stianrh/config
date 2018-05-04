let num =255 
while num >= 0
    let cul = 255 - num
    let r = 255 - cul
    let g = (cul*510/255)
    let b = (cul*255/255)
    if g>255
        let g = 510-g
    endif
    let rgb = 255*255*r+255*g+b
    let str = printf('#%06x', rgb)
    exec 'hi col_'.str.' ctermbg='.str.' ctermfg=white'
    echo 'hi col_'.str.' ctermbg='.str.' ctermfg=white'
    exec 'syn match col_'.str.' "ctermbg='.str.':...." containedIn=ALL'
    echo 'syn match col_'.str.' "ctermbg='.str.':...." containedIn=ALL'
    call append(0, 'ctermbg='.str.':....')
    let num = num - 1
endwhile
