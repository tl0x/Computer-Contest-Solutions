def solve(n, src, dest, ind):
    if n == 1:
        print(src + dest)
        return
    solve(n - 1, src, ind, dest)
    solve(1, src, dest, ind)
    solve(n - 1, ind, dest, src)


n = int(input())
solve(n, "A", "C", "B")
