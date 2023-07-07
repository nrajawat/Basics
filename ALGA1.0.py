import streamlit as st
import time

def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return Quick_Sort(left) + middle + Quick_Sort(right)

def Bubble_Sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

     # Print the sorted array
    x = " ".join(map(str, arr))
    return x

import streamlit as st

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = Merge_Sort(left)
    right = Merge_Sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def Selection_Sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def Heap_Sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
def Insertion_Sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def main():
    st.title("ALgorithm Analysis Application")
    st.subheader("Sorting and Running Time Calculator")
    st.info("Different Sorting Algorithm for Running Time Analysis")
    st.subheader("Sort the Array")

    # Create a text area input for array elements
    input_str = st.text_area("Enter array elements separated by commas")

    # Convert the input string into an array
    arr = [int(x) for x in input_str.split(",") if x.strip() != ""]

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Bubble Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_array = Bubble_Sort(arr)
                end_time = time.time()
                # Print the sorted array
                st.write("Sorted array:", sorted_array)
                running_time = end_time - start_time
                st.write("Running time:", running_time, "seconds")


        if st.button("Heap Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_arr = Heap_Sort(arr)
                end_time = time.time()
                # Print the sorted array
                st.write("Sorted array:", sorted_arr)
                running_time = end_time - start_time
                st.write("Running time:", running_time, "seconds")


    with col2:
        if st.button("Quick Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_array = Quick_Sort(arr)
                end_time = time.time()
                # Print the sorted array
                st.write("Sorted array:", sorted_array)
                running_time = end_time - start_time
                st.write("Running time:", running_time, "seconds")

        if st.button("Merge Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_arr = Merge_Sort(arr)
                end_time = time.time()
                # Print the sorted array
                st.write("Sorted array:", sorted_arr)
                running_time = end_time - start_time
                st.write("Running time:", running_time, "seconds")



    with col3:
        if st.button("Insertion Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_arr = Insertion_Sort(arr)
                end_time = time.time()

            # Print the sorted array
            st.write("Sorted array:", sorted_arr)

            # Print the running time
            running_time = end_time - start_time
            st.write("Running time:", running_time, "seconds")

        if st.button("Selection Sort"):
            if len(arr) == 0:
                st.write("No valid input provided.")
            else:
                start_time = time.time()
                sorted_arr = Selection_Sort(arr)
                end_time = time.time()
                # Print the sorted array
                st.write("Sorted array:", sorted_arr)

                # Print the running time
                running_time = end_time - start_time
                st.write("Running time:", running_time, "seconds")




    st.sidebar.subheader("About the App")
    st.sidebar.text("ALgorithm Application")
    st.sidebar.markdown(""" 
    #### Description  
    This is an ALgorithm Analysis Application based on Streamlit. 
    It is useful for Sorting Elements and analyzing Running time""")


    st.sidebar.subheader(" By")
    st.sidebar.text("Neelima Rajawat")
    st.sidebar.text("MS in Artificial Intelligence")
    st.sidebar.text("Florida Atlantic University")

if __name__ == '__main__':
    main()
