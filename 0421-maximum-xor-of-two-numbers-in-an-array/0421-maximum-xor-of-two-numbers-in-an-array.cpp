#include <iostream>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode() : children(2, nullptr) {}
    vector<TrieNode*> children;
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        TrieNode* root = new TrieNode();
        
        for (int num : nums) {
            TrieNode* curr = root;
            for (int shifter = 31; shifter >= 0; shifter--) {
                int bit = (num >> shifter) & 1;
                if (!curr->children[bit]) {
                    curr->children[bit] = new TrieNode();
                }
                curr = curr->children[bit];
            }
        }
        
        int ans = 0;
        for (int num : nums) {
            TrieNode* curr = root;
            int temp = 0;
            for (int shifter = 31; shifter >= 0; shifter--) {
                int bit = (num >> shifter) & 1;
                int val = 0;
                int comp = 1 - bit;
                if (curr->children[comp]) {
                    val = comp;
                    curr = curr->children[comp];
                } else {
                    val = bit;
                    curr = curr->children[bit];
                }
                temp <<= 1;
                temp |= val;
            }
            ans = max(ans, num ^ temp);
        }
        
        return ans;
    }
};
