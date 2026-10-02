with open("docode.txt", "r", encoding="utf-8") as f:
    new = f.read()
new = new.replace("&", "&amp;")
new = new.replace(">", "&gt;")
new = new.replace("<", "&lt;")
new = new.replace("```cpp", '<pre><code class="language-cpp">})')
new = new.replace("```", "</code></pre>")
with open("docode.txt", "w", encoding="utf-8") as file:
    file.write(new)