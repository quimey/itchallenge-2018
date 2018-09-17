x ="""edbbaacdcaacacbababaabadeeeaaddecaaeceeecbdcdaeacaccccaddeaaddecdcdcdccadcacceeecdcbceecebde
dadbccabcdeccbcdbedaaabbdccdddcbdbebdeca
aeaeddabaacbdcecacccbbacededbecbaccdccccebacdbbaedecbaeadaebedeccbaedcdcdabdcedbddabaeeaadcbdd
abbdaedeeeedeaeeabcabbadbebedcedaadabbbddbbebdabecdcbdcc
cddddabbaeaccaabedebbaaeabccecddcdbaaecbeeadeaeadabeddadaccbcdeebcacceaddabccdccaaddddd
bbeeabcadeecbcadae
dcbaceaadbdeceaaccaaeecadeedabeaecadbbebeecbdcddaadbbdbeecaaebcadddbb
adcdeaccccaaeabaaeaaabeaecdbadbabdecadeeacebcdcceceebeecdeaeebbbccaeacedeaeddbd
ed
ebeecaddbbceecebdeadedecddddecddecebeabbbecabdbeddeceabc"""
res = []
for y in x.split('\n'):
    s = 0
    for i in range(len(y)):
        z = y[i:]
        j = 0
        while j < len(z) and z[j] == y[j]:
            j += 1
            s += 1
    print y,s
    res.append(str(s))
print ' '.join(res)
