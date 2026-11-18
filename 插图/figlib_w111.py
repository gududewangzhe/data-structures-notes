# -*- coding: utf-8 -*-
"""数据结构 第十一周第一节 · TikZ 图源（5 张）。"""

FIGS = {
    'w111_01': r"""\begin{tikzpicture}[scale=0.95]
\node[font=\scriptsize,anchor=west] at (0.00,1.30) {insert 35 into 30 -> 41 -> 33};
\node (n30) at (1.60,0.60) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {30};
\node (n41) at (2.75,0.60) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {41};
\node (n33) at (2.05,-0.45) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {33};
\node (n35) at (3.05,-0.45) [circle,draw,thick,fill=red!15,inner sep=1.4pt,font=\scriptsize] {35};
\draw[thick] (n30)--(n41);
\draw[thick] (n41)--(n33);
\draw[thick,red] (n33)--(n35);
\node[font=\tiny,red,anchor=west] at (3.30,-0.45) {new};
\node[font=\tiny,gray,anchor=west] at (-0.05,0.60) {T};
\node[font=\tiny,gray,anchor=west] at (4.10,0.60) {35 > 30, go right};
\node[font=\tiny,gray,anchor=west] at (4.10,-0.10) {35 < 41, go left};
\node[font=\tiny,gray,anchor=west] at (4.10,-0.70) {35 > 33, go right = NULL};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.30) {return order: create(35) -> hang on 33.rchild -> 33 -> hang on 41.lchild -> 41 -> hang on 30.rchild};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.65) {every return carries the (possibly new) subtree root back to its parent};
\node[font=\tiny,gray,anchor=west] at (-0.05,-2.00) {without these assignments the new node would have no way back into the tree};
\end{tikzpicture}""",
    'w111_02': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,1.45) {build a BST by inserting 50, 30, 70, 20, 40, 60, 80 in this order};
\node (a)  at (2.40,0.90) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {50};
\node (b)  at (1.40,0.00) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {30};
\node (c)  at (3.40,0.00) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {70};
\node (d)  at (0.85,-0.90) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {20};
\node (e)  at (1.95,-0.90) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {40};
\node (f)  at (2.85,-0.90) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {60};
\node (g)  at (3.95,-0.90) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {80};
\draw[thick] (a)--(b); \draw[thick] (a)--(c);
\draw[thick] (b)--(d); \draw[thick] (b)--(e);
\draw[thick] (c)--(f); \draw[thick] (c)--(g);
\node[font=\tiny,red] at (2.62,0.92) {1};
\node[font=\tiny,red] at (1.06,0.05) {2};
\node[font=\tiny,red] at (3.72,0.05) {3};
\node[font=\tiny,red] at (0.52,-0.85) {4};
\node[font=\tiny,red] at (2.20,-0.85) {5};
\node[font=\tiny,red] at (2.52,-0.85) {6};
\node[font=\tiny,red] at (4.20,-0.85) {7};
\node[font=\tiny,gray,anchor=west] at (4.60,0.90) {red number = insertion order};
\node[font=\tiny,gray,anchor=west] at (4.60,0.55) {inorder: 20 30 40 50 60 70 80};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.55) {every new node lands on a leaf: no existing node is moved or relinked};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.90) {the shape depends on the insertion order: start from 20, 30, 40 ... and you get a right-leaning chain};
\end{tikzpicture}""",
    'w111_03': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,1.55) {delete P with two children: copy S->data into P->data, then delete S};
\node (P) at (1.60,0.85) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {P};
\node (L) at (0.70,0.00) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {L};
\node (R) at (2.50,0.00) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {R};
\node (S) at (2.05,-0.85) [circle,draw,thick,fill=green!12,inner sep=1.4pt,font=\scriptsize] {S};
\node (Q) at (2.95,-0.85) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {Q};
\draw[thick] (P)--(L); \draw[thick] (P)--(R);
\draw[thick] (R)--(S);
\node[font=\tiny,gray,anchor=west] at (3.30,-0.85) {S = leftmost in R, so S.lchild = NULL};
\node[font=\tiny,gray,anchor=west] at (3.30,-1.20) {step 1: P.data = S.data};
\node[font=\tiny,gray,anchor=west] at (3.30,-1.55) {step 2: delete S = case 2 (at most one child)};
\node[font=\tiny,gray,anchor=west] at (3.30,-1.90) {P itself is never unlinked: only three nodes involved};
\node[font=\tiny,gray,anchor=west] at (-0.05,-2.45) {compare: the naive way needs F, P, S, Q and two separate algorithms};
\node[font=\tiny,gray,anchor=west] at (-0.05,-2.80) {this way needs only P, S, Q and one algorithm};
\end{tikzpicture}""",
    'w111_04': r"""\begin{tikzpicture}[scale=0.92]
\node[font=\scriptsize,anchor=west] at (0.00,1.75) {extended binary tree: circles = internal nodes, boxes = external nodes};
\node (a) at (2.20,1.05) [circle,draw,thick,fill=white,inner sep=1.5pt,font=\scriptsize] {A};
\node (b) at (1.20,0.10) [circle,draw,thick,fill=white,inner sep=1.5pt,font=\scriptsize] {B};
\node (c) at (3.20,0.10) [circle,draw,thick,fill=white,inner sep=1.5pt,font=\scriptsize] {C};
\node (x1) at (0.55,-0.85) [rectangle,draw,thick,fill=gray!12,minimum size=0.40cm,font=\scriptsize] {};
\node (x2) at (1.85,-0.85) [rectangle,draw,thick,fill=gray!12,minimum size=0.40cm,font=\scriptsize] {};
\node (x3) at (2.55,-0.85) [rectangle,draw,thick,fill=gray!12,minimum size=0.40cm,font=\scriptsize] {};
\node (x4) at (3.85,-0.85) [rectangle,draw,thick,fill=gray!12,minimum size=0.40cm,font=\scriptsize] {};
\draw[thick] (a)--(b); \draw[thick] (a)--(c);
\draw[thick] (b)--(x1); \draw[thick] (b)--(x2);
\draw[thick] (c)--(x3); \draw[thick] (c)--(x4);
\node[font=\tiny,gray,anchor=west] at (4.35,1.05) {internal nodes: A, B, C  (n = 3)};
\node[font=\tiny,gray,anchor=west] at (4.35,0.70) {external nodes: 4 boxes  (n + 1 = 4)};
\node[font=\tiny,gray,anchor=west] at (4.35,0.35) {I = 0 + 1 + 1 = 2};
\node[font=\tiny,gray,anchor=west] at (4.35,0.00) {E = 2+2+2+2 = 8 = I + 2n};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.55) {every internal node has exactly two children once the null slots are drawn as boxes};
\node[font=\tiny,gray,anchor=west] at (-0.05,-1.90) {so E - I = 2n always, and minimizing I is the same as minimizing E};
\end{tikzpicture}""",
    'w111_05': r"""\begin{tikzpicture}[scale=0.90]
% step 1: 2,3 -> 5
\node[font=\scriptsize,anchor=west] at (0.00,1.85) {step 1: take 2 and 3};
\node (p5) at (1.30,1.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {5};
\node (l2) at (0.75,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {2};
\node (l3) at (1.85,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {3};
\draw[thick] (p5)--(l2); \draw[thick] (p5)--(l3);
\node[font=\tiny,gray,anchor=west] at (0.00,0.15) {small on the left};
% step 2: 5,6 -> 11
\node[font=\scriptsize,anchor=west] at (3.20,1.85) {step 2: take 5 and 6};
\node (q11) at (4.60,1.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {11};
\node (q5)  at (4.05,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {5};
\node (q6)  at (5.15,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {6};
\node (q2)  at (3.70,-0.60) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {2};
\node (q3)  at (4.40,-0.60) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {3};
\draw[thick] (q11)--(q5); \draw[thick] (q11)--(q6);
\draw[thick] (q5)--(q2); \draw[thick] (q5)--(q3);
\node[font=\tiny,gray,anchor=west] at (3.20,0.15) {5 stays on the left};
% step 3: 11,8 -> 19
\node[font=\scriptsize,anchor=west] at (6.60,1.85) {step 3: take 8 and 11};
\node (r19) at (8.00,1.10) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {19};
\node (r8)  at (7.45,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {8};
\node (r11) at (8.55,0.25) [circle,draw,thick,fill=white,inner sep=1.4pt,font=\scriptsize] {11};
\node (r5)  at (8.10,-0.60) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {5};
\node (r6)  at (9.00,-0.60) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {6};
\node (r2)  at (7.75,-1.45) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {2};
\node (r3)  at (8.45,-1.45) [circle,draw,thick,fill=white,inner sep=1.3pt,font=\scriptsize] {3};
\draw[thick] (r19)--(r8); \draw[thick] (r19)--(r11);
\draw[thick] (r11)--(r5); \draw[thick] (r11)--(r6);
\draw[thick] (r5)--(r2); \draw[thick] (r5)--(r3);
\node[font=\tiny,gray,anchor=west] at (6.60,0.15) {8 < 11, so 8 on the left};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.15) {WPL = 2x3 + 3x3 + 6x2 + 8x1 = 6 + 9 + 12 + 8 = 35};
\node[font=\tiny,gray,anchor=west] at (0.00,-2.50) {every merge puts the smaller root on the left, never changes side};
\end{tikzpicture}""",
}
