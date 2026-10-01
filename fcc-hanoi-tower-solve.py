def hanoi_solver(disks: int):
    #rods from left to right
    rod1 = list(range(disks,0,-1))
    rod2 = []
    rod3 = []
    positions_list = f"{rod1} {rod2} {rod3}\n"

    def solve(n, source, spare, target):
        nonlocal positions_list
        if n <= 0:
            return
        solve(n - 1, source, target, spare) #
        target.append(source.pop())
        positions_list += f"{rod1} {rod2} {rod3}\n"
        solve(n - 1, spare, source, target)

    solve(disks, rod1, rod2, rod3)

    return positions_list[0:len(positions_list)-1]
print(hanoi_solver(2))
