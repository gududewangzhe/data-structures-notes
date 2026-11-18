# -*- coding: utf-8 -*-
"""数据结构 第九周第二节 二叉树的遍历 · TikZ 图源（4 张）。

把 FIGS 里任意一条放进 Markdown 的 ```tikz 代码块即可重新渲染；
正式讲义里用的是 _讲义插图/svg/ 下的同名 .svg 矢量文件。
硬约束：源码纯 ASCII；坐标不得嵌套括号；\foreach 体内算式整体加括号。
"""

FIGS = {
    'w92_01_tree': r"""\begin{tikzpicture}[scale=0.95]
\node (A) at (2.80,0.00) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {A};
\node (B) at (1.75,-0.85) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {B};
\node (C) at (3.85,-0.85) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {C};
\node (D) at (1.15,-1.70) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {D};
\node (E) at (2.40,-1.70) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {E};
\node (F) at (3.25,-1.70) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {F};
\node (I) at (4.45,-1.70) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {I};
\node (G) at (0.80,-2.55) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {G};
\node (H) at (2.75,-2.55) [circle,draw,thick,fill=white,inner sep=1.6pt,font=\scriptsize] {H};
\draw[thick] (A)--(B); \draw[thick] (A)--(C);
\draw[thick] (B)--(D); \draw[thick] (B)--(E);
\draw[thick] (D)--(G);
\draw[thick] (E)--(H);
\draw[thick] (C)--(F); \draw[thick] (C)--(I);
\draw[dashed,gray] (0.50,-0.58) rectangle (2.96,-2.88);
\draw[dashed,gray] (3.00,-0.58) rectangle (5.05,-2.06);
\node[font=\scriptsize,red] at (0.66,-0.75) {2};
\node[font=\scriptsize,red] at (3.16,-0.75) {3};
\node[font=\scriptsize,red] at (3.50,-0.30) {1};
\node[font=\scriptsize,anchor=west] at (5.30,0.30) {1  root: A};
\node[font=\scriptsize,anchor=west] at (5.30,-0.05) {2  left subtree of A};
\node[font=\scriptsize,anchor=west] at (5.30,-0.40) {3  right subtree of A};
\node[font=\tiny,gray,anchor=west] at (5.30,-1.10) {preorder  = 1 2 3};
\node[font=\tiny,gray,anchor=west] at (5.30,-1.45) {inorder   = 2 1 3};
\node[font=\tiny,gray,anchor=west] at (5.30,-1.80) {postorder = 2 3 1};
\node[font=\tiny,gray,anchor=west] at (5.30,-2.45) {the three orders differ ONLY in where};
\node[font=\tiny,gray,anchor=west] at (5.30,-2.75) {the root block 1 is placed};
\node[font=\tiny,gray,anchor=west] at (0.50,-3.20) {nine nodes: D has only a left child, E only a right child, F and I are leaves};
\end{tikzpicture}""",
    'w92_02_orders': r"""\begin{tikzpicture}[scale=0.90]
\node[font=\scriptsize,anchor=west] at (0.00,0.75) {preorder  DLR};
\node (a1) at (2.55,0.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b1) at (1.60,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (c1) at (3.50,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {C};
\node (d1) at (1.05,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (e1) at (2.15,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {E};
\node (f1) at (3.00,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {F};
\node (i1) at (4.10,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {I};
\node (g1) at (0.75,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\node (h1) at (2.50,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {H};
\draw[thick] (a1)--(b1); \draw[thick] (a1)--(c1);
\draw[thick] (b1)--(d1); \draw[thick] (b1)--(e1);
\draw[thick] (d1)--(g1); \draw[thick] (e1)--(h1);
\draw[thick] (c1)--(f1); \draw[thick] (c1)--(i1);
\node[font=\tiny,red] at (2.88,0.10) {1};
\node[font=\tiny,red] at (1.93,-0.70) {2};
\node[font=\tiny,red] at (1.38,-1.50) {3};
\node[font=\tiny,red] at (1.08,-2.30) {4};
\node[font=\tiny,red] at (2.48,-1.50) {5};
\node[font=\tiny,red] at (2.83,-2.30) {6};
\node[font=\tiny,red] at (3.83,-0.70) {7};
\node[font=\tiny,red] at (3.33,-1.50) {8};
\node[font=\tiny,red] at (4.43,-1.50) {9};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.85) {A B D G E H C F I};
\node[font=\scriptsize,anchor=west] at (5.60,0.75) {inorder  LDR};
\node (a2) at (8.15,0.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b2) at (7.20,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (c2) at (9.10,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {C};
\node (d2) at (6.65,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (e2) at (7.75,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {E};
\node (f2) at (8.60,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {F};
\node (i2) at (9.70,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {I};
\node (g2) at (6.35,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\node (h2) at (8.10,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {H};
\draw[thick] (a2)--(b2); \draw[thick] (a2)--(c2);
\draw[thick] (b2)--(d2); \draw[thick] (b2)--(e2);
\draw[thick] (d2)--(g2); \draw[thick] (e2)--(h2);
\draw[thick] (c2)--(f2); \draw[thick] (c2)--(i2);
\node[font=\tiny,red] at (6.68,-2.30) {1};
\node[font=\tiny,red] at (6.98,-1.50) {2};
\node[font=\tiny,red] at (7.53,-0.70) {3};
\node[font=\tiny,red] at (8.08,-1.50) {4};
\node[font=\tiny,red] at (8.43,-2.30) {5};
\node[font=\tiny,red] at (8.48,0.10) {6};
\node[font=\tiny,red] at (8.93,-1.50) {7};
\node[font=\tiny,red] at (9.43,-0.70) {8};
\node[font=\tiny,red] at (10.03,-1.50) {9};
\node[font=\tiny,gray,anchor=west] at (5.60,-2.85) {G D B E H A F C I};
\node[font=\scriptsize,anchor=west] at (11.30,0.75) {postorder  LRD};
\node (a3) at (13.85,0.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b3) at (12.90,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (c3) at (14.80,-0.70) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {C};
\node (d3) at (12.35,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (e3) at (13.45,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {E};
\node (f3) at (14.30,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {F};
\node (i3) at (15.40,-1.50) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {I};
\node (g3) at (12.05,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\node (h3) at (13.80,-2.30) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {H};
\draw[thick] (a3)--(b3); \draw[thick] (a3)--(c3);
\draw[thick] (b3)--(d3); \draw[thick] (b3)--(e3);
\draw[thick] (d3)--(g3); \draw[thick] (e3)--(h3);
\draw[thick] (c3)--(f3); \draw[thick] (c3)--(i3);
\node[font=\tiny,red] at (12.38,-2.30) {1};
\node[font=\tiny,red] at (12.68,-1.50) {2};
\node[font=\tiny,red] at (14.13,-2.30) {3};
\node[font=\tiny,red] at (13.78,-1.50) {4};
\node[font=\tiny,red] at (13.23,-0.70) {5};
\node[font=\tiny,red] at (14.63,-1.50) {6};
\node[font=\tiny,red] at (15.73,-1.50) {7};
\node[font=\tiny,red] at (15.13,-0.70) {8};
\node[font=\tiny,red] at (14.18,0.10) {9};
\node[font=\tiny,gray,anchor=west] at (11.30,-2.85) {G D H E B F I C A};
\end{tikzpicture}""",
    'w92_03_stack': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,1.95) {the recursion stack while descending along A, B, D, G};
\node[font=\tiny,gray,anchor=west] at (0.00,1.55) {each entry = a node whose subtree is still unfinished};
\node[font=\tiny,gray,anchor=west] at (0.00,1.25) {stack depth = depth of the current node; the deepest stack = the height of the tree};
\foreach \cx/\lab in {0.00/call A, 2.10/call B, 4.20/call D, 6.30/call G}{
  \draw[thick] (\cx,-2.00) rectangle (\cx+1.55,-1.58);
  \node[font=\tiny,gray] at (\cx+0.775,-2.22) {\lab};
}
\draw[thick] (0.00,-1.58) rectangle (1.55,-1.16);
\node[font=\scriptsize] at (0.775,-1.37) {A};
\draw[thick] (2.10,-1.58) rectangle (3.65,-1.16);
\node[font=\scriptsize] at (2.875,-1.37) {A};
\draw[thick] (2.10,-1.16) rectangle (3.65,-0.74);
\node[font=\scriptsize] at (2.875,-0.95) {B};
\draw[thick] (4.20,-1.58) rectangle (5.75,-1.16);
\node[font=\scriptsize] at (4.975,-1.37) {A};
\draw[thick] (4.20,-1.16) rectangle (5.75,-0.74);
\node[font=\scriptsize] at (4.975,-0.95) {B};
\draw[thick] (4.20,-0.74) rectangle (5.75,-0.32);
\node[font=\scriptsize] at (4.975,-0.53) {D};
\draw[thick] (6.30,-1.58) rectangle (7.85,-1.16);
\node[font=\scriptsize] at (7.075,-1.37) {A};
\draw[thick] (6.30,-1.16) rectangle (7.85,-0.74);
\node[font=\scriptsize] at (7.075,-0.95) {B};
\draw[thick] (6.30,-0.74) rectangle (7.85,-0.32);
\node[font=\scriptsize] at (7.075,-0.53) {D};
\draw[thick] (6.30,-0.32) rectangle (7.85,0.10);
\node[font=\scriptsize] at (7.175,-0.11) {G};
\node[font=\tiny,red,anchor=west] at (8.15,-0.11) {top cell = current node (G)};
\draw[->,thick] (1.60,-0.80) -- (2.05,-0.80);
\draw[->,thick] (3.70,-0.80) -- (4.15,-0.80);
\draw[->,thick] (5.80,-0.80) -- (6.25,-0.80);
\node[font=\tiny,gray,anchor=west] at (0.00,-2.62) {going back from G: pop G, pop D; but B still has its right subtree E, H to finish};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.94) {so the extra space is O(h), and in the worst case (a single-branch tree) h = n, i.e. O(n)};
\end{tikzpicture}""",
    'w92_04_reverse': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.20,1.00) {1 going down};
\node[font=\scriptsize,anchor=west] at (4.40,1.00) {2 after reversing};
\node[font=\scriptsize,anchor=west] at (8.60,1.00) {3 on the way back};
\node (a1) at (1.60,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b1) at (1.20,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (d1) at (0.80,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (g1) at (0.45,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\draw[->,thick] (a1)--(b1); \draw[->,thick] (b1)--(d1); \draw[->,thick] (d1)--(g1);
\node[font=\tiny,red,anchor=west] at (1.85,-0.55) {down, no stack};
\node (a2) at (4.90,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b2) at (4.50,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (d2) at (4.10,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (g2) at (3.75,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\draw[->,thick,red] (g2)--(d2); \draw[->,thick,red] (d2)--(b2); \draw[->,thick,red] (b2)--(a2);
\node[font=\tiny,red,anchor=west] at (5.15,-0.55) {up the same links};
\node (a3) at (9.10,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {A};
\node (b3) at (8.70,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {B};
\node (d3) at (8.30,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {D};
\node (g3) at (7.95,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {G};
\draw[->,thick,blue] (a3)--(b3); \draw[->,thick,blue] (b3)--(d3); \draw[->,thick,blue] (d3)--(g3);
\node[font=\tiny,blue,anchor=west] at (9.35,-0.55) {restored};
\node[font=\tiny,gray,anchor=west] at (0.20,-3.05) {from G you can walk back to D, to B, to A without any stack: a stack of size h is saved};
\node[font=\tiny,gray,anchor=west] at (0.20,-3.40) {but ONE field now means "child" when going down and "parent" when coming up};
\node[font=\tiny,gray,anchor=west] at (0.20,-3.75) {so a flag is needed to tell which is which (a threaded tree uses flags for another purpose)};
\end{tikzpicture}""",
}
