# Fork description

this repo add a new function for latexify to get latex from a plain text

e.g.：
``` python
import latexify
code = {
   "name":"f",
   "args":"x",
   "code":"return x"
}
output = latexify.get_latex_with_code(name = code["name"], args = code["args"], code = code["code"])
print(output)
```
stdout:  
f(x) = x

- Why not contribute to latexify？
   - In fact, Sympy have the same feature(sympy.latex), so it's not necessary for official latexify have this feature.
