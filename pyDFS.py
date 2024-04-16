"""
  DFS(Deapth-First-Search)
  : 다차원 배열에서 각 칸을 방문할 때 깊이를 우선으로 방문하는 알고리즘
    그래프라는 자료구조에서 모든 노드를 방문하기 위한 알고리즘

  1. 시작하는 칸을 스택에 넣고 방문했다는 표시를 남김
  2. 스택에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
  3. 해당 칸을 이전에 방문했다면 아무것도 하지 않고, 처음으로 방문했다면 방문했다는 표시를남기고 해당 칸을 스택에 삽입
  4. 스택이 빌 때까지 2번을 반복, 모든 칸이 스택에 1번씩 들어가므로 시간복잡도는 칸이 N개일 때 O(N)
  x 가 열 y 가 행
"""