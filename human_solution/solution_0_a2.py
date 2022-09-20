def main():
    test_cases = int(input())
    for i in range(test_cases):
        if check():
            print("Yes")
        else:
            print("No")

def check():
    beanstalk_levels = int(input())
    leaves_at_level = []
    leaves_at_level[0:] = list(map(int, input().split()))
    expected_leaves = 0.5
    for j in range(len(leaves_at_level)):
        expected_leaves = 2 * expected_leaves - leaves_at_level[j]
    return expected_leaves == 0

if __name__=="__main__":
    main() 
