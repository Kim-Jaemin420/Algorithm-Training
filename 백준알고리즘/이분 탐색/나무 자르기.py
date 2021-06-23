N, M = map(int, input().split())
H = list(map(int, input().split()))


H.sort()
sp = 0
ep = H[N - 1]


def cut_tree(sp, ep):
    while sp <= ep:
        md = (sp + ep) // 2
        tree_h = 0
        for t in H:
            if t > md:
                tree_h += t - md
        if tree_h > M:
            sp = md + 1
        elif tree_h < M:
            ep = md - 1
        elif tree_h == M:
            return md

    if sp > ep:
        if tree_h >= M:
            return md
        while tree_h < M:
            tree_h = 0
            md -= 1
            for t in H:
                if t > md:
                    tree_h += t - md
        return md


res = cut_tree(sp, ep)

print(res)
