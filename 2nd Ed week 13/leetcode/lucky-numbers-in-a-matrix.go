func luckyNumbers (matrix [][]int) []int {
    n := len(matrix)
    m := len(matrix[0])

    var minimums []int
    var maximums []int

    for i:=0; i < n; i++ {
        cur_min := matrix[i][0]
        for j := 1; j < m; j++{
            if cur_min >= matrix[i][j]{
                cur_min = matrix[i][j]
            }
        }
        minimums = append(minimums, cur_min)
    }
    
    for j := 0; j < m; j++{
        cur_max := matrix[0][j]
        for i := 1; i < n; i++{
            if cur_max < matrix[i][j]{
                cur_max = matrix[i][j]
            }
        }
        maximums = append(maximums, cur_max)
    }

    var answer []int
    
    for i := 0; i < n; i++{
        for j := 0; j < m; j++{
            if matrix[i][j] == minimums[i] && matrix[i][j] == maximums[j]{
                answer = append(answer, matrix[i][j])
            }
        }
    }

    return answer
}