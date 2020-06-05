# Results

The following shows the output of our solver for the three riddles that were given as examples in the introduction. Per riddle every part seperated by the lines sequentially represents a time in the riddle where a different amount of information is available. The last part for every riddle thus represents the moment where all the information from the riddle is given.

## Muddy Children

Do any of the children know whether they are muddy?

```plain
K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r

OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r)))))))

(M, 7) ⊭ K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r
```

---------------------------------------------------------------------------------------

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


## Drinking Logicians

After the barman has asked whether everybody wants a drink, and after agent A announces he does not know whether everybody wants a drink, is it common knowledge that agent A wants a drink?

```plain
[~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp

Box[NOT(OR(K{A}(AND(p, AND(q, r))), K{A}(NOT(AND(p, AND(q, r))))))](C(p))

(M, 7) ⊨ [~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp
```

------------------------------------------------------------------------------------------------------------

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
-----------------------------------------------------------------------------------------------------------------

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
