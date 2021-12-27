public class MinStack {

    class Node
    {
        public int Value {get; set;}
        public Node NextSmallestNode {get; set;}
    }
    
    private readonly Stack<Node> _stack;
    
    public MinStack() {
        _stack = new Stack<Node>();
    }
    
    public void Push(int val) {
        if (_stack.Any())
        {
            var node = new Node();
            node.Value = val;
            
            var top = _stack.Peek();
            if (val < top.NextSmallestNode.Value)
            {
                node.NextSmallestNode = node;
            }
            else
            {
                node.NextSmallestNode = top.NextSmallestNode;
            }
            
            _stack.Push(node);
        }
        else
        {
            var node = new Node();
            node.Value = val;
            node.NextSmallestNode = node;
            _stack.Push(node);
        }
    }
    
    public void Pop() {
        _stack.Pop();
    }
    
    public int Top() {
        return _stack.Peek().Value;
    }
    
    public int GetMin() {
        return _stack.Peek().NextSmallestNode.Value;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */