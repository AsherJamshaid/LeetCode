class ProductOfNumbers {
private:
    vector<int> prefix;
    vector<int> stream;
public:
    ProductOfNumbers() {
        prefix.push_back(1);
    }
    
    void add(int num) {
        stream.push_back(num);

        if (num == 0) {
            prefix.clear();
            prefix.push_back(1);
        } else {
            int last = prefix[prefix.size() - 1];
            prefix.push_back(last * num);
        }
    }
    
    int getProduct(int k) {
        if (k >= (int)prefix.size()) {
            return 0;
        }

        int n = prefix.size();
        int result = prefix[n - 1] / prefix[n - 1 - k];
        return result;
    }
    
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
