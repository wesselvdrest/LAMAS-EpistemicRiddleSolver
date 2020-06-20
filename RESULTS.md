# Results

The following shows the output of our solver for the three riddles that were given as examples in the introduction. Per riddle every part seperated by the lines sequentially represents a time in the riddle where a different amount of information is available. The last part for every riddle thus represents the moment where all the information from the riddle is given.

## Muddy Children
Three brilliant children go to the park to play. When their father comes to find them, he sees that all of them have mud on their foreheads. He then says, “At least one of you has mud on your forehead”, and then asks, “Do you know if you have mud on your forehead?” The children simultaneously respond, “No”.
Do any of the children know whether they are muddy?

```plain
K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r

OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r)))))))

(M, 7) ⊭ K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r
```
--------------------------------------------------------------------------------------------------------------------

After the first announcement that at least one child is muddy. Do any of the children know whether they are muddy?

```plain
<p|q|r>(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Diamond<OR(p, OR(q, r))>(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))

(M, 7) ⊭ <p|q|r>(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
-------------------------------------------------------------------------------------------------------------------

No one has stepped forward yet, which can be represented as an announcement. After the second announcement that at least one child is muddy, do any of the children know whether they are muddy?

```plain
[(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Box[OR(p, OR(q, r))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r)))))))))

(M, 7) ⊭ [(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
--------------------------------------------------------------------------------------------------------------------

No one has stepped forward yet, which can be represented as an announcement. After the third announcement that at least one child is muddy, do any of the children know whether they are muddy?

```plain
[(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Box[OR(p, OR(q, r))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))))

(M, 7) ⊨ [(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
--------------------------------------------------------------------------------------------------------------------


## Drinking Logicians
Three logicians walk into a bar. The barman says, 'Does everybody want a drink?' The first logician says, 'I don't know.' The second logician says, 'I don't know.' What does the third logician say?

After the barman has asked whether everybody wants a drink, and after agent A announces he does not know whether everybody wants a drink, is it common knowledge that agent A wants a drink?

```plain
[~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp

Box[NOT(OR(K{A}(AND(p, AND(q, r))), K{A}(NOT(AND(p, AND(q, r))))))](C(p))

(M, 7) ⊨ [~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp
```
--------------------------------------------------------------------------------------------------------------------

After the barman has asked whether everybody wants a drink, and after agent A and agent B announce that they do not know whether everybody wants a drink, does agent C know whether everybody wants a drink?

```plain
[~(K{A}(p&q&r)|K{A}~(p&q&r))&~(K{B}(p&q&r)|K{B}~(p&q&r))]K{C}(p&q&r)

Box[AND(NOT(OR(K{A}(AND(p, AND(q, r))), K{A}(NOT(AND(p, AND(q, r)))))), NOT(OR(K{B}(AND(p, AND(q, r))), K{B}(NOT(AND(p, AND(q, r)))))))](K{C}(AND(p, AND(q, r))))

(M, 7) ⊨ [~(K{A}(p&q&r)|K{A}~(p&q&r))&~(K{B}(p&q&r)|K{B}~(p&q&r))]K{C}(p&q&r)
```

## Cheryl's Birthday

Does anyone know Cheryls birthday?

```plain
K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v)|K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v)

OR(K{A}(AND(p, x)), OR(K{A}(AND(p, y)), OR(K{A}(AND(q, v)), OR(K{A}(AND(q, y)), OR(K{A}(AND(r, v)), OR(K{A}(AND(r, x)), OR(K{A}(AND(s, w)), OR(K{A}(AND(s, y)), OR(K{A}(AND(t, w)), OR(K{A}(AND(u, v)), OR(K{B}(AND(p, x)), OR(K{B}(AND(p, y)), OR(K{B}(AND(q, v)), OR(K{B}(AND(q, y)), OR(K{B}(AND(r, v)), OR(K{B}(AND(r, x)), OR(K{B}(AND(s, w)), OR(K{B}(AND(s, y)), OR(K{B}(AND(t, w)), K{B}(AND(u, v)))))))))))))))))))))

(M, 5) ⊭ K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v)|K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v)
```
---------------------------------------------------------------------------------------------------------------------

Cheryl tells Albert that the month of her birthday is july and Bernard that the day of her birthday is 16

```plain
[K{A}((p&x)|(r&x))&K{B}((r&v)|(r&x))](K{A}(r&x)&K{B}(r&x))

Box[AND(K{A}(OR(AND(p, x), AND(r, x))), K{B}(OR(AND(r, v), AND(r, x))))](AND(K{A}(AND(r, x)), K{B}(AND(r, x))))

(M, 5) ⊨ [K{A}((p&x)|(r&x))&K{B}((r&v)|(r&x))](K{A}(r&x)&K{B}(r&x))
```
--------------------------------------------------------------------------------------------------------------------  

Albert announces that he does not know cheryls birthday and he knows that Bernard does not know it

```plain
<K{A}(p&x|r&x)&K{A}K{B}(r&v|r&x)>[K{A}((p&x)|(r&x))&K{B}((r&v)|(r&x))](K{A}(r&x)&K{B}(r&x))

Diamond<AND(K{A}(AND(p, OR(x, AND(r, x)))), K{A}(K{B}(AND(r, OR(v, AND(r, x))))))>(Box[AND(K{A}(OR(AND(p, x), AND(r, x))), K{B}(OR(AND(r, v), AND(r, x))))](AND(K{A}(AND(r, x)), K{B}(AND(r, x)))))

(M, 5) ⊭ <K{A}(p&x|r&x)&K{A}K{B}(r&v|r&x)>[K{A}((p&x)|(r&x))&K{B}((r&v)|(r&x))](K{A}(r&x)&K{B}(r&x))
```
--------------------------------------------------------------------------------------------------------------------  

Albert and Bernard both announce that they know cheryls birthday, do they know her birthday now?

```plain
<K{A}(r&x)&K{B}(r&x)>[K{A}(r&x)&K{A}K{B}(r&x)&K{B}(r&x)](K{A}(r&x)&K{B}(r&x))

Diamond<AND(K{A}(AND(r, x)), K{B}(AND(r, x)))>(Box[AND(K{A}(AND(r, x)), AND(K{A}(K{B}(AND(r, x))), K{B}(AND(r, x))))](AND(K{A}(AND(r, x)), K{B}(AND(r, x)))))

(M, 5) ⊭ <K{A}(r&x)&K{B}(r&x)>[K{A}(r&x)&K{A}K{B}(r&x)&K{B}(r&x)](K{A}(r&x)&K{B}(r&x))
```
-----------------------------------------------------------------------------------------------------------------------  

After all the announcements do both Albert and Bernard know Cheryls birthday?
```plain
[K{A}(r&x)&K{A}K{B}(r&x)&K{B}(r&x)&K{B}K{A}(r&x)](K{A}(r&x)&K{B}(r&x))

Box[AND(K{A}(AND(r, x)), AND(K{A}(K{B}(AND(r, x))), AND(K{B}(AND(r, x)), K{B}(K{A}(AND(r, x))))))](AND(K{A}(AND(r, x)), K{B}(AND(r, x))))

(M, 5) ⊨ [K{A}(r&x)&K{A}K{B}(r&x)&K{B}(r&x)&K{B}K{A}(r&x)](K{A}(r&x)&K{B}(r&x))
```
--------------------------------------------------------------------------------------------------------------------

## Consecutive Numbers
Anne and Bill are each going to be told a natural number. Their numbers will be one apart. The numbers are now being whispered in their respective ears. They are aware of this scenario. Suppose Anne is told 2 and Bill is told 3. The following truthful conversation between Anne and Bill now takes place: Anne: "I do not know your number." Bill: "I do not know your number." Anne: "I know your number." Bill: "I know your number." 

Does Anne know Bill's number?

```plain
K{A}p|K{A}r

OR(K{A}(p), K{A}(r))

(M, 1) ⊭ K{A}p|K{A}r
```
-----------------------------------------------------------------------------------------------------------------------  

 Does Bill know Anne's number?
```plain
K{B}q|K{B}s

OR(K{B}(q), K{B}(s))

(M, 1) ⊭ K{B}q|K{B}s
```
-----------------------------------------------------------------------------------------------------------------------  

Is it true that Bill does not know Anne's number after she says she does not know Bill's number?
```plain
[~K{A}(p)&~K{A}(r)](~K{B}(q)&~K{B}(s))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](AND(NOT(K{B}(q)), NOT(K{B}(s))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)](~K{B}(q)&~K{B}(s))
```
-----------------------------------------------------------------------------------------------------------------------  

Does Anne know Bill's number after Bill announces he does not know hers?

```plain
[~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)](K{A}(p)|K{A}(r))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](Box[AND(NOT(K{B}(q)), NOT(K{B}(s)))](OR(K{A}(p), K{A}(r))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)](K{A}(p)|K{A}(r))
```
-----------------------------------------------------------------------------------------------------------------------  

 Does Bill know Anne's number after Anne has announced that she knows his?

```plain
[~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)][K{A}(p)|K{A}(r)](K{B}(q)|K{B}(s))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](Box[AND(NOT(K{B}(q)), NOT(K{B}(s)))](Box[OR(K{A}(p), K{A}(r))](OR(K{B}(q), K{B}(s)))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)][K{A}(p)|K{A}(r)](K{B}(q)|K{B}(s))
```
-----------------------------------------------------------------------------------------------------------------------  

## Hangman
At a trial a prisoner is sentenced to death. The verdict reads "You will be executed next week, but the day on which you will be executed is a surprise to you." The prisoner reasons as follows. "I cannot be executed on Friday, because in that case I would not be surprised. But given that Friday is eliminated, then I cannot be executed on Thursday either, because that would then no longer be a surprise. And so on. Therefore the verdict cannot be executed." And so, his execution, that happened to be on Wednesday, came as a surprise.  

Does the prisoner know on which day he will be executed?
```plain
K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g

OR(K{P}(a), OR(K{P}(b), OR(K{P}(c), OR(K{P}(d), OR(K{P}(e), OR(K{P}(f), K{P}(g)))))))

(M, 2) ⊭ K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g
```
-----------------------------------------------------------------------------------------------------------------------  

After the announcement by the judge, does the prisoner know he will not be executed on Friday, thereby making his reasoning correct?

```plain
[(a|b|c|d|e|f|g)&~(K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g)](K{P}e)

Box[AND(OR(a, OR(b, OR(c, OR(d, OR(e, OR(f, g)))))), NOT(OR(K{P}(a), OR(K{P}(b), OR(K{P}(c), OR(K{P}(d), OR(K{P}(e), OR(K{P}(f), K{P}(g)))))))))](K{P}(e))

(M, 2) ⊭ [(a|b|c|d|e|f|g)&~(K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g)](K{P}e)
```
-----------------------------------------------------------------------------------------------------------------------  
Is the prisoner screwed?

```plain
a|b|c|d|e|f|g

OR(a, OR(b, OR(c, OR(d, OR(e, OR(f, g))))))

(M, 2) ⊨ a|b|c|d|e|f|g
```
-----------------------------------------------------------------------------------------------------------------------  