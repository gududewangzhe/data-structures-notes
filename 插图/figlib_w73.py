# -*- coding: utf-8 -*-
"""第七周第三节插图：二维地址两步数法 / 下三角映射 / 三对角映射。追加进共享图库。"""
import io, os, json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
LIB = r"C:\Users\lizix\Documents\Obsidian Vault\数据结构\_讲义插图"
F, C = {}, {}


def add(k, cap, src):
    F[k] = src.strip()
    C[k] = cap


# A1 二维地址公式的两步数法
add("A1_two_steps", "二维地址公式的两步数法：取第 I 行第 J 列，先把上面 I−1 行整片数掉（蓝），再把本行前 J−1 个补上（绿），红格就是目标。两块相加即偏移量。", r"""
\begin{tikzpicture}[scale=0.92]
  \foreach \r in {1,2,3,4}{
    \foreach \c in {1,2,3,4,5}{
      \draw[thick] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
    }
  }
  \foreach \r in {1,2}{
    \foreach \c in {1,2,3,4,5}{
      \draw[fill=blue!12,thick] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
    }
  }
  \foreach \c in {1,2,3}{
    \draw[fill=green!20,thick] (\c*0.80,{(4-3)*0.70}) rectangle ++(0.80,0.70);
  }
  \draw[fill=red!25,thick] (4*0.80,{(4-3)*0.70}) rectangle ++(0.80,0.70);
  \node[font=\scriptsize] at (4*0.80+0.40,{(4-3)*0.70+0.35}) {$J$};
  \node[font=\scriptsize] at (1*0.80+0.40,{(4-3)*0.70+0.35}) {$I$};
  \foreach \c in {1,2,3,4,5}{
    \node[font=\tiny,gray] at (\c*0.80+0.40,{(4-1)*0.70+0.85}) {\c};
  }
  \foreach \r in {1,2,3,4}{
    \node[font=\tiny,gray] at (0.45,{(4-\r)*0.70+0.35}) {\r};
  }
  \node[below,font=\small] at (2.80,-0.30) {blue: $(I-C_1)\times(D_2-C_2+1)$ cells above};
  \node[below,font=\small] at (2.80,-0.80) {green: $(J-C_2)$ cells before it in row $I$};
  \node[below,font=\small] at (2.80,-1.30) {sum the two, multiply by $L$, add $la$};
\end{tikzpicture}
""")

# A2 下三角映射到一维
add("A2_lower_tri", "下三角矩阵按下标压缩：上三角那半根本不存，只把下三角按行优先排成一条一维数组。第 I 行第 J 列的位置就是「前 I−1 行之和 + 行内第 J−1 个」。", r"""
\begin{tikzpicture}[scale=0.92]
  \foreach \r in {1,2,3,4}{
    \foreach \c in {1,2,3,4}{
      \ifnum\c>\r
        \draw[gray!45,dashed] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
      \else
        \draw[thick] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
      \fi
    }
  }
  \node[font=\scriptsize] at (0.40,{(4-2)*0.70+0.35}) {rows};
  \foreach \r/\k in {1/1,2/3,3/6,4/10}{
    \foreach \c in {1,...,\r}{
      \node[font=\scriptsize] at (\c*0.80+0.40,{(4-\r)*0.70+0.35}) {\k};
      \pgfmathsetmacro{\k}{\k+1}
    }
  }
  \node[below,font=\small] at (2.00,-0.35) {dashed upper part is never stored};
  \node[below,font=\small] at (2.00,-0.85) {row 1 has 1, row 2 has 2, row 3 has 3, row 4 has 4};
  \node[below,font=\small] at (2.00,-1.35) {offset $=(I-1)I/2+(J-1)$, counting from 1};
\end{tikzpicture}
""")

# A3 三对角映射
add("A3_tridiag", "三对角矩阵只有三条对角线有元素：主对角线加上下各一条。按行优先压缩时，首行只有 2 个、第二行 3 个、其余每行 3 个，所以偏移化简成 2I+J−3。", r"""
\begin{tikzpicture}[scale=0.92]
  \foreach \r in {1,2,3,4}{
    \foreach \c in {1,2,3,4}{
      \ifnum\c=\r
        \draw[fill=red!18,thick] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
      \else
        \pgfmathparse{int(abs(\c-\r))}
        \ifnum\pgfmathresult=1
          \draw[fill=blue!14,thick] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
        \else
          \draw[gray!45,dashed] (\c*0.80,{(4-\r)*0.70}) rectangle ++(0.80,0.70);
        \fi
      \fi
    }
  }
  \node[font=\scriptsize] at (0.40,{(4-1)*0.70+0.35}) {1};
  \node[font=\scriptsize] at (0.40,{(4-2)*0.70+0.35}) {2};
  \node[font=\scriptsize] at (0.40,{(4-3)*0.70+0.35}) {3};
  \node[font=\scriptsize] at (0.40,{(4-4)*0.70+0.35}) {4};
  \node[below,font=\small] at (2.00,-0.35) {red: main diagonal, blue: the two neighbours};
  \node[below,font=\small] at (2.00,-0.85) {row 1 keeps 2 cells, rows 2 and 3 keep 3, row 4 keeps 2};
  \node[below,font=\small] at (2.00,-1.35) {offset $=[3(I-1)-1]+(J-I+1)=2I+J-3$};
\end{tikzpicture}
""")

p = os.path.join(LIB, "tikz_lib.json")
d = json.load(io.open(p, encoding="utf-8"))
d["figures"].update(F)
d["captions"].update(C)
io.open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2))

bad = [(k, ch) for k, v in F.items() for ch in v if ord(ch) > 0xFF]
print("新增:", len(F), "| 纯 ASCII:", not bad, "| 图库:", len(d["figures"]))
if bad:
    print("!!", bad)
