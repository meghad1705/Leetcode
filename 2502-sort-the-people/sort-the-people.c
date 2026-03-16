char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {
    
    for(int i = 0; i < heightsSize - 1; i++){
        for(int j = 0; j < heightsSize - i - 1; j++){
            
            if(heights[j] < heights[j+1]){

                // swap heights
                int tempH = heights[j];
                heights[j] = heights[j+1];
                heights[j+1] = tempH;

                // swap corresponding names
                char* tempN = names[j];
                names[j] = names[j+1];
                names[j+1] = tempN;
            }
        }
    }

    *returnSize = namesSize;
    return names;
}
