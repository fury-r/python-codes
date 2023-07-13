def designerPdfViewer(h, word):
    d=sorted([[k,h[ord(k)-ord('a')]] for k in word ],key=lambda item:item[1],reverse=True)
    
    return d[0][1]*len(word)