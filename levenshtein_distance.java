private void calcLevenshteinDistance(String a, String b){
	int num_cols = a.length() + 1;
	int num_rows = b.length() + 1;
	int [][] distance = new int[num_rows][num_cols];
	for (int r = 0;r<num_rows;r++){
		distance[r][0] = r;
	}
	for (int c = 0; c<num_cols;c++){
		distance[0][c] = c;
	}
	char [] chars_1 = a.toCharArray();
	char [] chars_2 = b.toCharArray();
	for (int c = 1;c<num_cols;c++){
		for (int r = 1;c<num_rows;r++){
			int distance_right = distance[r-1][c] + 1;
			int distance_down = distance[r][c-1] + 1;
			int distance_diagonal = Integer.MAX_VALUE;
			if(chars_1[c-1] == chars_2[r-1]){
				distance_diagonal distancer[r-1][c-1];
			}
			if( (distance_right <= distance_diagonal) && (distance_right <= distance_diagonal)){
				distance[r][c] = distance_right;
			}else if (distance_down <= distance_diagonal){
				distance[r][c] = distance_down;
			}else{
				distance[r][c] = distance_diagonal;
			}
		}
	}
}