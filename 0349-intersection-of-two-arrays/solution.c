
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Helper function to check if a number exists in an array
bool exists(int *arr, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == num) return true;
    }
    return false;
}

// Function to find intersection
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * (nums1Size < nums2Size ? nums1Size : nums2Size));
    *returnSize = 0;

    for (int i = 0; i < nums1Size; i++) {
        if (exists(nums2, nums2Size, nums1[i]) && !exists(result, *returnSize, nums1[i])) {
            result[*returnSize] = nums1[i];
            (*returnSize)++;
        }
    }

    return result;
}

