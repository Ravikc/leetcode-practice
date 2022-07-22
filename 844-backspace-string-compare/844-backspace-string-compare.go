func backspaceCompare(s string, t string) bool {
    sStack := []rune{}
    tStack := []rune{}

    for _, c := range s {
        if c == '#' {
            if len(sStack) > 0 {
                sStack = sStack[:len(sStack) - 1]                
            }
        } else {
            sStack = append(sStack, c)
        }
    }
    
    for _, c := range t {
        if c == '#' {
            if len(tStack) > 0 {
                tStack = tStack[:len(tStack) - 1]                
            }
        } else {
            tStack = append(tStack, c)
        }
    }
    
    return string(sStack) == string(tStack)
}