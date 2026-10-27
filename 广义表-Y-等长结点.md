# 广义表 $Y=(a,(b,c,d),e)$ 的等长结点链接存储示意图

![广义表-Y-等长结点](插图/广义表-Y-等长结点.svg)

```tikz
\usetikzlibrary{shapes.multipart,positioning}
\begin{document}
\begin{tikzpicture}[
    >=latex,
    cell/.style={
        draw,
        rectangle split,
        rectangle split horizontal,
        rectangle split parts=3,
        rectangle split part align=center,
        minimum height=10mm,
        inner sep=3pt,
        font=\small
    },
    ptr/.style={->,thick}
]

% Level 1: a -> (b,c,d) -> e
\node[cell] (a) at (0,0) {
    0 \nodepart{two} $a$ \nodepart{three}  {}
};
\node[cell] (sub) at (3.5,0) {
    1 \nodepart{two}  {} \nodepart{three}  {}
};
\node[cell] (e) at (7,0) {
    0 \nodepart{two} $e$ \nodepart{three} $\wedge$
};

% Sublist (b,c,d): b -> c -> d
\node[cell] (b) at (3.5,-2.8) {
    0 \nodepart{two} $b$ \nodepart{three}  {}
};
\node[cell] (c) at (7,-2.8) {
    0 \nodepart{two} $c$ \nodepart{three}  {}
};
\node[cell] (d) at (10.5,-2.8) {
    0 \nodepart{two} $d$ \nodepart{three} $\wedge$
};

% Entry pointer
\node[font=\large] (Y) at (-2,0) {$Y$};
\draw[ptr] (Y.east) -- (a.west);

% tp pointers on level 1
\draw[ptr] (a.three east) -- (sub.west);
\draw[ptr] (sub.three east) -- (e.west);

% hp pointer of the list node to the first sublist node b
\draw[ptr] (sub.two south) -- (b.north);

% tp pointers inside the sublist
\draw[ptr] (b.three east) -- (c.west);
\draw[ptr] (c.three east) -- (d.west);

\end{tikzpicture}
\end{document}
```
