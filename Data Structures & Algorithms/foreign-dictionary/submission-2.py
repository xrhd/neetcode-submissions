class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges, nodes = build_graph(words)
        if not nodes:
            return ""
        sorted_nodes, has_cycle = top_sort(edges, nodes)
        return "" if has_cycle else "".join(sorted_nodes)

def get_edge(a: str, b: str) -> Tuple[str, str]:
    M = min(len(a), len(b))
    for i in range(M):
        if a[i] != b[i]:
            return (a[i], b[i])
    if len(a) > len(b):
        return None  # a é prefixo de b e é maior -> inválido
    return None  # sem relação de ordem

def build_graph(words) -> Tuple[List, List]:
    # Inicializar com TODAS as letras únicas
    nodes = list(set("".join(words)))
    edges = []
    for a, b in zip(words[:-1], words[1:]):
        edge = get_edge(a, b)
        if edge is None:
            # Verificar se é o caso inválido de prefixo
            if len(a) > len(b) and a[:len(b)] == b:
                return None, None
            continue
        edges.append(edge)
    return edges, nodes

def dfs(node, adj, visited, path, sorted_nodes):
    if node in path:
        return True
    if node in visited:
        return False

    visited.add(node)
    path.add(node)
    for node_adj in adj.get(node, []):
        if dfs(node_adj, adj, visited, path, sorted_nodes):
            return True

    path.remove(node)
    sorted_nodes.append(node)
    return False

def top_sort(edges, nodes):
    adj = {node: set() for node in nodes}
    for a, b in edges:
        adj[a].add(b)

    visited, path = set(), set()
    sorted_nodes, has_cycle = [], False
    for node in nodes:
        if dfs(node, adj, visited, path, sorted_nodes):
            has_cycle = True
            break

    sorted_nodes.reverse()
    return sorted_nodes, has_cycle