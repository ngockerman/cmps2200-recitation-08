# CMPS 2200 Recitation 08

## Answers

**Name:** Natalie Gockerman
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
- Work:
- each vertex is push/pop maximum of 1 time at best distance and relax each edge once
- heap operations cost O(log |v|)
- Therefore: W = O((|V|+|E|)log|V|)
- Span:
- algorithm is fully sequential
- span is same as work
- Therfore: S = O((|V|+|E|)log|V|)

- **2b)**
- Bfs-path:
-   standard BFS that maintains a pointer to parent while discovering new nodes
-   O(1) for parent pointer per vertex
-   Work:
-     O(|V|+|E|) because each vertex is queue/dequeue once and each edge examined once
-   Span:
-     all sequential, span same
-     O(|V|+|E|)
- Get_path:
-   moves bachward from destinatino to source and reverses
-   k = number of vertexes on path
-   moving backwards through parents --> k entries --> O(k)
-   reversing length of k --> O(k)
-   Work:
-     O(k), worst case O(|V|)
-   Span:
-     sequential
-     O(k), worst case O(|V|)

