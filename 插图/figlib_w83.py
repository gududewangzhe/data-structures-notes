# -*- coding: utf-8 -*-
"""数据结构 第八周第三节 树与二叉树 · TikZ 图源（11 张）。

用法：把 FIGS 里任意一条源码放进 Markdown 的 ```tikz 代码块即可重新渲染；
渲染成独立文件见 _讲义插图/svg/ 。
硬约束：源码必须纯 ASCII（TikZJax 只吃 Latin-1，且无中文）；
坐标不得嵌套括号；\foreach 体内算式要整体加括号。
"""

FIGS = {
    'w83_01_tree': r"""\begin{tikzpicture}[scale=0.95,every node/.style={fill=white,draw,circle,inner sep=1.6pt,font=\scriptsize}]
\node (A) at (0,0) {A};
\node (B) at (-3.4,-1.15) {B};
\node (C) at (0,-1.15) {C};
\node (D) at (3.4,-1.15) {D};
\node (E) at (-4.5,-2.30) {E};
\node (F) at (-2.1,-2.30) {F};
\node (G) at (0,-2.30) {G};
\node (H) at (2.2,-2.30) {H};
\node (I) at (3.5,-2.30) {I};
\node (J) at (4.8,-2.30) {J};
\node (K) at (-5.1,-3.45) {K};
\node (L) at (-3.9,-3.45) {L};
\node (M) at (2.2,-3.45) {M};
\draw (A) -- (B);
\draw (A) -- (C);
\draw (A) -- (D);
\draw (B) -- (E);
\draw (B) -- (F);
\draw (E) -- (K);
\draw (E) -- (L);
\draw (C) -- (G);
\draw (D) -- (H);
\draw (D) -- (I);
\draw (D) -- (J);
\draw (H) -- (M);
\end{tikzpicture}""",
    'w83_02_venn': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (-2.60,1.90) {nested sets = parenthesis form: the same tree};
\draw[thick] (-0.10,-0.10) ellipse (2.55 and 1.45);
\node[font=\scriptsize] at (-0.10,1.16) {A};
\draw[thick] (-1.55,-0.25) ellipse (0.85 and 0.62);
\node[font=\scriptsize] at (-1.55,0.22) {B};
\draw[thick] (-1.72,-0.62) ellipse (0.42 and 0.20);
\node[font=\tiny] at (-1.72,-0.62) {E};
\node[font=\tiny] at (-1.05,-0.45) {F};
\draw[thick] (0.55,-0.20) ellipse (0.62 and 0.45);
\node[font=\scriptsize] at (0.55,0.14) {C};
\node[font=\tiny] at (0.55,-0.24) {G};
\draw[thick] (1.55,-0.88) ellipse (0.58 and 0.40);
\node[font=\scriptsize] at (1.55,-0.66) {D};
\node[font=\tiny] at (1.42,-1.02) {H};
\node[font=\tiny] at (1.55,-1.02) {I};
\node[font=\tiny] at (1.68,-1.02) {J};
\node[font=\tiny,gray,anchor=west] at (-2.60,-2.00) {a closed region is a set; nesting is containment};
\node[font=\scriptsize,anchor=west] at (3.20,0.85) {Venn diagram:};
\node[font=\scriptsize,anchor=west] at (3.20,0.45) {a closed region};
\node[font=\scriptsize,anchor=west] at (3.20,0.05) {means containment};
\node[font=\scriptsize,anchor=west] at (3.20,-0.35) {shape does not matter};
\node[font=\scriptsize,anchor=west] at (3.20,-1.00) {Parenthesis form:};
\node[font=\scriptsize,anchor=west] at (3.20,-1.40) {A(B(E(K,L),F),C(G),D(H,I,J,M))};
\node[font=\tiny,gray,anchor=west] at (3.20,-1.85) {outer brackets = root; each sibling pair = a child};
\end{tikzpicture}""",
    'w83_03_indent': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\tiny,gray,anchor=west] at (0.00,0.35) {indentation = level; same indentation = siblings};
\node[anchor=west,font=\scriptsize] at (0.05,0.00) {A};
\node[anchor=west,font=\scriptsize] at (0.85,-0.52) {B};
\node[anchor=west,font=\scriptsize] at (1.65,-1.04) {E};
\node[anchor=west,font=\scriptsize] at (2.45,-1.56) {K};
\node[anchor=west,font=\scriptsize] at (2.45,-2.08) {L};
\node[anchor=west,font=\scriptsize] at (1.65,-2.60) {F};
\node[anchor=west,font=\scriptsize] at (0.85,-3.12) {C};
\node[anchor=west,font=\scriptsize] at (1.65,-3.64) {G};
\node[anchor=west,font=\scriptsize] at (0.85,-4.16) {D};
\node[anchor=west,font=\scriptsize] at (1.65,-4.68) {H};
\node[anchor=west,font=\scriptsize] at (2.45,-5.20) {M};
\node[anchor=west,font=\scriptsize] at (1.65,-5.72) {I};
\node[anchor=west,font=\scriptsize] at (1.65,-6.24) {J};
\node[font=\tiny,gray,anchor=west] at (4.45,0.00) {level 1};
\node[font=\tiny,gray,anchor=west] at (4.45,-0.52) {level 2};
\node[font=\tiny,gray,anchor=west] at (4.45,-1.04) {level 3};
\node[font=\tiny,gray,anchor=west] at (4.45,-1.56) {level 4};
\node[font=\tiny,gray,anchor=west] at (4.45,-2.08) {level 4};
\node[font=\tiny,gray,anchor=west] at (4.45,-2.60) {level 3};
\node[font=\tiny,gray,anchor=west] at (4.45,-3.12) {level 2};
\node[font=\tiny,gray,anchor=west] at (4.45,-3.64) {level 3};
\node[font=\tiny,gray,anchor=west] at (4.45,-4.16) {level 2};
\node[font=\tiny,gray,anchor=west] at (4.45,-4.68) {level 3};
\node[font=\tiny,gray,anchor=west] at (4.45,-5.20) {level 4};
\node[font=\tiny,gray,anchor=west] at (4.45,-5.72) {level 3};
\node[font=\tiny,gray,anchor=west] at (4.45,-6.24) {level 3};
\foreach \y in {0.00,-0.52,-1.04,-1.56,-2.08,-2.60,-3.12,-3.64,-4.16,-4.68,-5.20,-5.72,-6.24}{
  \draw[gray!40] (0.00,\y-0.28) -- (4.25,\y-0.28);
}
\draw[gray!55,dashed] (0.58,0.25) -- (0.58,-6.55);
\draw[gray!55,dashed] (1.38,0.25) -- (1.38,-6.55);
\draw[gray!55,dashed] (2.18,0.25) -- (2.18,-6.55);
\end{tikzpicture}""",
    'w83_04_parent': r"""\begin{tikzpicture}[scale=0.92]
\node (A) at (0,0) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {A};
\node (B) at (-1.75,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {B};
\node (C) at (0,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {C};
\node (D) at (1.75,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {D};
\node (E) at (-2.30,-1.70) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {E};
\node (F) at (-1.20,-1.70) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {F};
\draw (A)--(B); \draw (A)--(C); \draw (A)--(D);
\draw (B)--(E); \draw (B)--(F);
\node[font=\tiny,gray,anchor=west] at (-2.55,-2.30) {the tree};
\foreach \r in {0.25,-0.10,-0.45,-0.80,-1.15,-1.50,-1.85}{
  \draw[thick] (3.20,\r) rectangle (5.85,\r-0.35);
}
\draw[thick] (4.05,0.25) -- (4.05,-1.85);
\draw[thick] (4.90,0.25) -- (4.90,-1.85);
\foreach \r/\a/\b in {0.25/idx/data, -0.10/1/A, -0.45/2/B, -0.80/3/C, -1.15/4/D, -1.50/5/E, -1.85/6/F}{
  \node[font=\scriptsize,anchor=west] at (3.28,\r-0.175) {\a};
  \node[font=\scriptsize,anchor=west] at (4.13,\r-0.175) {\b};
}
\node[font=\scriptsize,anchor=west] at (4.98,0.075) {parent};
\node[font=\scriptsize,anchor=west] at (4.98,-0.275) {0};
\node[font=\scriptsize,anchor=west] at (4.98,-0.625) {1};
\node[font=\scriptsize,anchor=west] at (4.98,-0.975) {1};
\node[font=\scriptsize,anchor=west] at (4.98,-1.325) {1};
\node[font=\scriptsize,anchor=west] at (4.98,-1.675) {2};
\node[font=\scriptsize,anchor=west] at (4.98,-2.025) {2};

\node[font=\tiny,gray,anchor=west] at (3.20,-2.40) {the parent field stores an INDEX, not an address: that is why this is a static structure};
\end{tikzpicture}""",
    'w83_05_nodelayout': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,0.45) {1. Fixed length (isomorphic): every node carries d pointers, d = degree of the tree = 3};
\draw[thick] (0.00,0.05) rectangle (1.05,-0.35);
\draw[thick] (1.05,0.05) rectangle (2.10,-0.35);
\draw[thick] (2.10,0.05) rectangle (3.15,-0.35);
\draw[thick] (3.15,0.05) rectangle (4.20,-0.35);
\node[font=\scriptsize] at (0.525,-0.15) {data};
\node[font=\scriptsize] at (1.575,-0.15) {child1};
\node[font=\scriptsize] at (2.625,-0.15) {child2};
\node[font=\scriptsize] at (3.675,-0.15) {child3};
\node[font=\tiny,gray,anchor=west] at (0.00,-0.75) {advantage: only ONE node type, easy to manage (uniform A4 paper)};
\node[font=\scriptsize,anchor=west] at (0.00,-1.40) {2. Variable length (non-isomorphic): a degree field tells how many pointers follow};
\draw[thick] (0.00,-1.80) rectangle (1.05,-2.20);
\draw[thick] (1.05,-1.80) rectangle (2.10,-2.20);
\draw[thick] (2.10,-1.80) rectangle (3.15,-2.20);
\draw[thick] (3.15,-1.80) rectangle (4.20,-2.20);
\draw[thick,dashed] (4.20,-1.80) rectangle (5.20,-2.20);
\node[font=\scriptsize] at (0.525,-2.00) {data};
\node[font=\scriptsize] at (1.575,-2.00) {degree};
\node[font=\scriptsize] at (2.625,-2.00) {child1};
\node[font=\scriptsize] at (3.675,-2.00) {child2};
\node[font=\scriptsize] at (4.700,-2.00) {child m};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.60) {m = degree of THIS node; degree = 0 means a leaf; the nodes have different sizes};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.95) {advantage: saves space. disadvantage: many node types, hard to manage (uneven sheets of paper)};
\end{tikzpicture}""",
    'w83_06_waste': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,0.75) {Case 1: family problem, d = 20, n = 10};
\foreach \i in {1,...,20}{
  \draw[thick,gray!70] (\i*0.26-0.26,0.35) rectangle (\i*0.26,-0.05);
}
\foreach \i in {1,...,3}{
  \draw[thick,blue] (\i*0.26-0.26,0.35) rectangle (\i*0.26,-0.05);
}
\node[font=\tiny,gray,anchor=west] at (0.00,-0.40) {blue = 3 children actually used; grey = 17 wasted slots on THIS node};
\node[font=\tiny,gray,anchor=west] at (0.00,-0.72) {empty chain fields in the whole tree = n(d-1)+1 = 10 times 19 plus 1 = 191};
\node[font=\scriptsize,anchor=west] at (0.00,-1.30) {Case 2: acquaintance relation, d = 1300000000 (one and a half billion)};
\foreach \i in {1,...,28}{
  \draw[thick,gray!70] (\i*0.19-0.19,-1.70) rectangle (\i*0.19,-2.10);
}
\draw[thick,blue] (0.00,-1.70) rectangle (0.19,-2.10);
\node[font=\tiny,gray,anchor=west] at (0.00,-2.45) {1 used, d-1 empty: the maximum is spread over EVERY node};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.77) {a long-tailed distribution always loses under a fixed-length layout};
\end{tikzpicture}""",
    'w83_07_childlist': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,0.95) {CTBox array (sequential) + child lists (linked); chain node = [child index | next]};
\foreach \c/\a/\b in {0.20/1/A, -0.40/2/B, -1.00/3/C, -1.60/4/D}{
  \draw[thick] (0.00,\c+0.20) rectangle (0.55,\c-0.20);
  \draw[thick] (0.55,\c+0.20) rectangle (1.15,\c-0.20);
  \draw[thick] (1.15,\c+0.20) rectangle (1.90,\c-0.20);
  \node[font=\scriptsize] at (0.275,\c) {\a};
  \node[font=\scriptsize] at (0.850,\c) {\b};
  \node[font=\tiny,gray] at (1.525,\c) {first};
}
\draw[->,thick] (1.94,0.20) -- (2.35,0.20);
\draw[thick] (2.40,0.40) rectangle (3.10,0.00);
\node[font=\scriptsize] at (2.75,0.20) {B=2};
\draw[thick] (3.10,0.40) rectangle (3.60,0.00);
\draw[->,thick] (3.64,0.20) -- (4.05,0.20);
\draw[thick] (4.10,0.40) rectangle (4.80,0.00);
\node[font=\scriptsize] at (4.45,0.20) {C=3};
\draw[thick] (4.80,0.40) rectangle (5.30,0.00);
\draw[->,thick] (5.34,0.20) -- (5.75,0.20);
\draw[thick] (5.80,0.40) rectangle (6.50,0.00);
\node[font=\scriptsize] at (6.15,0.20) {D=4};
\draw[thick] (6.50,0.40) rectangle (7.00,0.00);
\node[font=\tiny,gray] at (6.75,0.20) {nil};
\draw[->,thick] (1.94,-0.40) -- (2.35,-0.40);
\draw[thick] (2.40,-0.20) rectangle (3.10,-0.60);
\node[font=\scriptsize] at (2.75,-0.40) {E=5};
\draw[thick] (3.10,-0.20) rectangle (3.60,-0.60);
\draw[->,thick] (3.64,-0.40) -- (4.05,-0.40);
\draw[thick] (4.10,-0.20) rectangle (4.80,-0.60);
\node[font=\scriptsize] at (4.45,-0.40) {F=6};
\draw[thick] (4.80,-0.20) rectangle (5.30,-0.60);
\node[font=\tiny,gray] at (5.05,-0.40) {nil};
\draw[->,thick] (1.94,-1.00) -- (2.35,-1.00);
\node[font=\tiny,gray,anchor=west] at (2.50,-1.05) {nil   (C is a leaf, its child list is empty)};
\draw[->,thick] (1.94,-1.60) -- (2.35,-1.60);
\draw[thick] (2.40,-1.40) rectangle (3.10,-1.80);
\node[font=\scriptsize] at (2.75,-1.60) {G=7};
\draw[thick] (3.10,-1.40) rectangle (3.60,-1.80);
\node[font=\tiny,gray] at (3.35,-1.60) {nil};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.30) {each chain node stores the child INDEX, not a pointer to its data};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.62) {heads are sequential, children are linked: a combination of the two basic building blocks};
\end{tikzpicture}""",
    'w83_08_childsibling': r"""\begin{tikzpicture}[scale=0.92]
\node (A) at (0,0) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {A};
\node (B) at (-1.85,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {B};
\node (C) at (-0.62,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {C};
\node (D) at (0.62,-0.85) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {D};
\node (E) at (-2.30,-1.70) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {E};
\node (F) at (-1.40,-1.70) [circle,draw,fill=white,inner sep=1.6pt,font=\scriptsize] {F};
\draw (A)--(B); \draw (A)--(C); \draw (A)--(D);
\draw (B)--(E); \draw (B)--(F);
\node[font=\scriptsize,gray,anchor=west] at (-2.55,-2.30) {the tree};
%
\node[font=\small,anchor=west] at (2.55,0.55) {CSNode: data | firstchild | nextsibling};
\node (nA) at (3.55,-0.35) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {A};
\node (nB) at (3.55,-1.15) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {B};
\node (nC) at (4.85,-1.15) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {C};
\node (nD) at (6.15,-1.15) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {D};
\node (nE) at (3.55,-1.95) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {E};
\node (nF) at (4.85,-1.95) [rectangle,draw,thick,minimum width=0.55cm,minimum height=0.32cm,font=\scriptsize] {F};
\draw[->,thick] (nA) -- (nB);
\draw[->,thick,dashed] (nB) -- (nC);
\draw[->,thick,dashed] (nC) -- (nD);
\draw[->,thick] (nB) -- (nE);
\draw[->,thick,dashed] (nE) -- (nF);
\node[font=\tiny,gray,anchor=west] at (6.45,-1.10) {nil};
\node[font=\tiny,gray,anchor=west] at (5.15,-1.90) {nil};
\node[font=\tiny,gray,anchor=north] at (3.55,-2.55) {solid = firstchild};
\node[font=\tiny,gray,anchor=north] at (5.10,-2.55) {dashed = nextsibling};
\end{tikzpicture}""",
    'w83_09_fiveforms': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,0.75) {the five basic forms of a binary tree (Fig. 6.3 in the textbook)};
\draw[thick,dashed,gray] (0.05,-1.10) rectangle (1.20,-1.80);
\node[font=\tiny,gray] at (0.625,-1.45) {empty};
\node[font=\tiny,gray,anchor=north] at (0.625,-2.00) {1 empty};
\node (r2) at (2.625,-1.20) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {R};
\node[font=\tiny,gray,anchor=north] at (2.625,-2.00) {2 root only};
\node (r3) at (4.625,-1.20) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {R};
\node (l3) at (4.325,-1.80) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {L};
\draw (r3)--(l3);
\node[font=\tiny,gray,anchor=north] at (4.625,-2.00) {3 left only};
\node (r4) at (6.625,-1.20) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {R};
\node (rr4) at (6.925,-1.80) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {L};
\draw (r4)--(rr4);
\node[font=\tiny,gray,anchor=north] at (6.625,-2.00) {4 right only};
\node (r5) at (8.625,-1.20) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {R};
\node (a5) at (8.325,-1.80) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {L};
\node (b5) at (8.925,-1.80) [circle,draw,fill=white,inner sep=1.4pt,font=\scriptsize] {L};
\draw (r5)--(a5); \draw (r5)--(b5);
\node[font=\tiny,gray,anchor=north] at (8.625,-2.00) {5 both};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.55) {in 3 and 4 the missing side is EMPTY, not absent: the slot always exists};
\end{tikzpicture}""",
    'w83_10_fullcomplete': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,1.05) {Full binary tree, k = 3, 7 nodes};
\node (f1) at (1.75,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {1};
\node (f2) at (1.10,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {2};
\node (f3) at (2.40,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {3};
\node (f4) at (0.75,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {4};
\node (f5) at (1.45,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {5};
\node (f6) at (2.05,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {6};
\node (f7) at (2.75,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {7};
\draw (f1)--(f2); \draw (f1)--(f3);
\draw (f2)--(f4); \draw (f2)--(f5);
\draw (f3)--(f6); \draw (f3)--(f7);
\node[font=\tiny,gray,anchor=west] at (0.00,-2.05) {every level is full};
\node[font=\scriptsize,anchor=west] at (5.20,1.05) {Complete binary tree, k = 4, 10 nodes};
\node (g1) at (7.30,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {1};
\node (g2) at (6.65,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {2};
\node (g3) at (7.95,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {3};
\node (g4) at (6.30,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {4};
\node (g5) at (7.00,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {5};
\node (g6) at (7.60,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {6};
\node (g7) at (8.30,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {7};
\node (g8) at (6.30,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {8};
\node (g9) at (7.00,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {9};
\node (g10) at (7.60,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {10};
\draw (g1)--(g2); \draw (g1)--(g3);
\draw (g2)--(g4); \draw (g2)--(g5);
\draw (g3)--(g6); \draw (g3)--(g7);
\draw (g4)--(g8); \draw (g4)--(g9);
\draw (g5)--(g10);
\draw[thick,dashed,gray] (8.05,-2.15) rectangle (8.45,-2.55);
\node[font=\tiny,gray] at (8.25,-2.35) {11};
\draw[thick,dashed,gray] (8.65,-2.15) rectangle (9.05,-2.55);
\node[font=\tiny,gray] at (8.85,-2.35) {12};
\draw[thick,dashed,gray] (8.70,-1.25) rectangle (9.10,-1.65);
\node[font=\tiny,gray] at (8.90,-1.45) {13};
\node[font=\tiny,gray,anchor=west] at (5.20,-3.05) {top 3 levels full; last level filled left to right with no gap};
\node[font=\tiny,gray,anchor=west] at (5.20,-3.37) {dashed = the missing positions 11, 12, 13 of the full tree};
\node[font=\tiny,gray,anchor=west] at (0.00,-3.05) {complete = full tree cut off by number};
\end{tikzpicture}""",
    'w83_11_numbering': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,0.95) {level-order numbering of a complete binary tree with n = 10};
\node (c1) at (3.90,0.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {1};
\node (c2) at (3.25,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {2};
\node (c3) at (4.55,-0.55) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {3};
\node (c4) at (2.90,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {4};
\node (c5) at (3.60,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {5};
\node (c6) at (4.20,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {6};
\node (c7) at (4.90,-1.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {7};
\node (c8) at (2.90,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {8};
\node (c9) at (3.60,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {9};
\node (c10) at (4.20,-2.35) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {10};
\draw (c1)--(c2); \draw (c1)--(c3);
\draw (c2)--(c4); \draw (c2)--(c5);
\draw (c3)--(c6); \draw (c3)--(c7);
\draw (c4)--(c8); \draw (c4)--(c9);
\draw (c5)--(c10);
\node[font=\scriptsize,anchor=west] at (0.00,-3.05) {C array (index starts at 0)};
\foreach \k in {0,...,10}{
  \draw[thick] (0.55+\k*0.62,-3.45) rectangle (1.17+\k*0.62,-3.90);
}
\foreach \k in {1,...,10}{
  \node[font=\scriptsize] at (0.86+\k*0.62,-3.675) {\k};
}
\node[font=\tiny,gray] at (0.86,-3.675) {0};
\foreach \k in {0,...,10}{
  \node[font=\tiny,gray,anchor=north] at (0.86+\k*0.62,-3.98) {\k};
}
\node[font=\tiny,gray,anchor=west] at (0.00,-4.35) {node i is stored in a[i-1]: node 5 sits in slot 4, its left child 10 sits in slot 9};
\node[font=\tiny,gray,anchor=west] at (0.00,-4.67) {so the textbook formulas PARENT = floor(i/2), LEFT = 2i, RIGHT = 2i+1 all shift down by one in C code};
\end{tikzpicture}""",
}
