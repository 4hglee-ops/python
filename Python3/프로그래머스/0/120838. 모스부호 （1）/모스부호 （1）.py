def solution(letter):
    answer = ''
    word = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    for idx,text in enumerate(letter):
        if text == ' ':
            answer += morse[word]
            word =''
        elif idx == len(letter)-1:
            word += text
            answer += morse[word]
        else:
            word += text
    return answer