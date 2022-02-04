public class MinHeap
{
    private readonly int _size;
    private readonly IList<int> _list;
    public MinHeap(int size)
    {
        _size = size;
        _list = new List<int>(size);
    }
    
    private void Swap(int l, int r)
    {
        int temp = _list[l];
        _list[l] = _list[r];
        _list[r] = temp;
    }
    
    private void HeapifyBottomToTop(int index)
    {
        int parentIndex = (index - 1) / 2;
        if (parentIndex >= 0 && _list[parentIndex] > _list[index])
        {
            Swap(parentIndex, index);
            HeapifyBottomToTop(parentIndex);
        }
    }
    
    private void HeapifyTopToBottom(int index)
    {
        int leftIndex = (2 * index) + 1;
        if (leftIndex >= _list.Count)
        {
            return;
        }
        
        int rightIndex = (2 * index) + 2;
        
        int smallerIndex = leftIndex;
        if (rightIndex < _list.Count && _list[rightIndex] < _list[leftIndex])
        {
            smallerIndex = rightIndex;
        }
        
        if (_list[index] > _list[smallerIndex])
        {
            Swap(index, smallerIndex);
            HeapifyTopToBottom(smallerIndex);    
        }
        
        
        // if (_list.Count > leftIndex && _list[index] > _list[leftIndex])
        // {
        //     Swap(index, leftIndex);
        //     HeapifyTopToBottom(leftIndex);
        // }
        // else if (_list.Count > rightIndex && _list[index] > _list[rightIndex])
        // {
        //     Swap(index, rightIndex);
        //     HeapifyTopToBottom(rightIndex);
        // }
    }
    
    public int Add(int num)
    {
        if (_list.Count == _size)
        {
            if (num > _list.First())
            {
                _list[0] = num;
                HeapifyTopToBottom(0);
            }
        }
        else
        {
            _list.Add(num);
            HeapifyBottomToTop(_list.Count - 1);
        }
        
        return _list.First();
    }    
}


public class KthLargest {

    private readonly MinHeap _heap;
    public KthLargest(int k, int[] nums) {
        _heap = new MinHeap(k);
        foreach (int num in nums)
        {
            _heap.Add(num);
        }
    }
    
    public int Add(int val) {
        return _heap.Add(val);
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */