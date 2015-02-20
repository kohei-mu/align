import java.util.*;
import java.io.*;

public class align{

	public static void main(){
		//main function 


		//file open, readline, carry out execution function
		File file1 = new File("correct.txt");
		FileReader filereader1 = new FileReader(file1);
		BufferReader br1 = new BufferReader(filereader1);

		File file2 = new File("learner.txt");
		FileReader filereader2 = new FileReader(file2);
		BufferReader br2 = new BufferReader(filereader2);

		String f;
		Strgin j;


		File file3 = new File("output5.txt");
		FileWriter filewriter = new FileWriter(file3);

		while( ( (f = br1.readLine()) != null) || ((j = br2.readLine()) != null) ){
			filewriter.write(levenshtein(f,j));
		}

		br1.close();
		br2.close();
		filewriter.close();
	}

	public static void levenshtein(String str1,String str2){

		//make alignment
		//follow dp and give numbers

		String[] str1 = str1.split(" ", 0);
		String[] str2 = str2.split(" ", 0);

		int num_cols = str1.length() + 1;
		int num_rows = str2.length() + 1;
		int[][] distance = new int [num_rows][num_cols];
		for (int r = 0;r < num_rows;r++){
			distance[r][0] = r;
		}
		for (int c = 0;c < num_cols;c++){
			distance[0][c] = c;
		}
		char[] char1 = str1.toCharArray();
		char[] char2 = str2.toCharArray();
		int x;
		for (int c = 1; c < num_cols;c++){
			for(int r = 1;r < num_rows;r++){
				int [] min_list = new int[3]; 
				if (char1[c-1] == char2[r-1]){
					x = 0;
				}else{
					x = 1;
				}
				int a = Math.min(distance[r-1][c]+1, distance[r][c-1]+1);
				int b = Math.min(distance[r-1][c]+1, distance[r-1][c-1]+x);
				int c = Math.min(distance[r][c-1]+1, distance[r-1][c-1]+x);
				min_list[0] = a;
				min_list[1] = b;
				min_list[2] = c;
				int min = min_list[0]
				for (int i =0;i < min_list.length;++i){
					if(min > min_list[i]){
						min = min_list[i];
					}
				}
				distance[r][c] = min
			}
		} 
		List<String> str1_list = new ArrayList<String>();
		List<String> str2_list = new ArrayList<String>();

		int i = str1.length();
		int j = str2.length();

		List<int> count_null = new ArrayList<int>();
		int[][] dp = distance;

		if(i == j){
			int count = Math.max(i,j);
			for(int m = 1;m <= (Math.max(i,j)+8);m++){

				//caculate minumum number from dp
				int[] minimum_list = new int[3];
				minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
				minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
				minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
				int minimum = minimum_list[0];
				for(int i = 0; i < minimum_list.length();i++){
					if(minimum > minimum_list[i]){
						minimum = minimum_list[i];
					}
				}
				int num = minimum;


				if(i == 0) && (j == 0){
					break;
				}

				if(num == dp[i-1][j-1]){
					str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
					str2_list.add(str2[j-1]);
					count = count--;
					i = i--;
					j = j--;
				}else if(num == dp[i][j-1]){
					str2_list.add(str2[j-1]);
					j = j--;
				}else if(num == dp[i-1][j]){
					str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
					count = count--;
					i = i--;
				}

			}
			if(str2.length() < b.length()){
				List<String> str1_list = new ArrayList<String>();
				List<String> str2_list = new ArrayList<String>();
				int i = str1.length();
				int j = str2.length();
				List<int> count_null = new ArrayList<int>();
				int count = Math.max(i,j);
				for(int m = 1;m <= (Math.max(i,j)+8);m++){


					//caculate minumum number from dp
					int[] minimum_list = new int[3];
					minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
					minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
					minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
					int minimum = minimum_list[0];
					for(int i = 0; i < minimum_list.length();i++){
						if(minimum > minimum_list[i]){
							minimum = minimum_list[i];
						}
					}
					int num = minimum;


					if(num == dp[i-1][j-1]){
						if(i == 0) and (j == 0){
							break;
						}
						if(count > 0){
							str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
							count = count--;
						}
						str2_list.add(str2[j-1])
						i = i--;
						j = j--;
					}else if(num == dp[i][j-1]){
						if (j == 0){
							break;
						}
						if(count > 0){
							count_null.add(String.valueOf(count));
							count = count--;
						}
						str2_list.add(str2[j-1]);
						j = j--;
					}else if(num == dp[i-1][j]){
						if(i != 0){
							if(count == count){
								str1_list.add(str1[i-1]+" "+"({ })");
							}else{
								str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
								count = count--;
							}
							i = i--;
						}else if(i == 0){
							continue;
						}
					}

				}
			}
			//count_null = " ".join(count_null[::-1])+" "
			count_null = Collections.reverse(count_null);
			count_null = String.join(" ",count_null)+" ";
			if(count_null.length() > 1){
				str1_list.add("NULL ({ "+count_null+"})");
			}else{
				str1_list.add("NULL ({ })");
			}
		}else if(i < j){
			int count = Math.max(i,j);
			List<int> count_null = new ArrayList<int>();
			for(int m =1;m <= (max(i,j)+8);m++){

				//caculate minumum number from dp
				int[] minimum_list = new int[3];
				minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
				minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
				minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
				int minimum = minimum_list[0];
				for(int i = 0; i < minimum_list.length();i++){
					if(minimum > minimum_list[i]){
						minimum = minimum_list[i];
					}
				}
				int num = minimum;

				if(num == dp[i-1][j-1]){
					if((i == 0) || (j == 0)){
						break;
					}
					try{
						if(i != 0){
							str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
							str2_list.add(str2[j-1]);
							count = count--;
							i = i--;
							j = j--;
						}else if(i == 0){
							str2_list.add(str2[j-1]);
							j = j--;
						}
					}catch(Exception e){
							System.out.println("err");
						}
				}else if(num == dp[i][j-1]){
					if(j == 0){
						break;
					}
					if(count > 0){
						count_null.add(String.valueOf(count));
					}
					count = count--;
					if(j > 0){
						str2_list.add(str2[j-1]);
					}
					j = j--;
				}else if(num == dp[i-1][j]){
					if(i != 0){
						if(count == count){
							str1_list.add(str1[i-1]+" "+"({ })");
						}else{
							str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
							count = count--;
						}
						i = i--;
					}else if(i == 0){
						if(count > 0){
							count_null.add(String.valueOf(count));
							count = count--;
							if(j > 0){
								str2_list.add(str2[j-1]);
							}
							j = j--;
						}
					}
				}
			}
			if(str2.length() < b.length()){
				List<String> str1_list = new ArrayList<String>();
				List<String> str2_list = new ArrayList<String>();
				int i = str1.length();
				int j = str2.length();
				List<int> count_null = new ArrayList<int>();
				int count = Math.max(i,j);
				for(int m = 1;m <= (Math.max(i,j)+8);m++){

					//caculate minumum number from dp
					int[] minimum_list = new int[3];
					minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
					minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
					minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
					int minimum = minimum_list[0];
					for(int i = 0; i < minimum_list.length();i++){
						if(minimum > minimum_list[i]){
							minimum = minimum_list[i];
						}
					}
					int num = minimum;

					if(j == 0){
						break;
					}

					if(num == dp[i-1][j-1]){
						try{
							if(i != 0){
								str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
								str2_list.add(str2[j-1]);
								count = count--;
								i = i--;
								j = j--;
							}else if(i == 0){
								str2_list.add(str2[j-1]);
								j = j--;
							}
						}catch(Exception e){
							System.out.println("err");
						}
					}else if(num == dp[i][j-1]){
						if(count > 0){
							count_null.add(String.valueOf(count));
						}
						str2_list.add(str2[j-1]);
						j = j--;
					}else if(num == dp[i-1][j]){
						if(i != 0){
							if(count == count){
								str1_list.add(str1[i-1]+" "+"({ })");
							}else{
								str1_list.add(str1[i-1]+" "+"(`{ "+String.valueOf(count)+" })");
								count = count--;
							}
							i = i--;
						}else if(i == 0){
							continue;
						}
					}
				}
			}

			count_null = Collections.reverse(count_null);
			count_null = String.join(" ",count_null)+" ";
			if(count_null.length() > 1){
				str1_list.add("NULL ({ "+String.valueOf(count_null)+"})");
			}else{
				str1_list.add("NULL ({ })");
			}
		}else if(i > j){
			count = Math.min(i,j);
			List<int> count_null = new ArrayList<int>();
			for(int m = 1;m <= (Math.max(i,j)+8);m++){

				//caculate minumum number from dp
				int[] minimum_list = new int[3];
				minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
				minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
				minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
				int minimum = minimum_list[0];
				for(int i = 0; i < minimum_list.length();i++){
					if(minimum > minimum_list[i]){
						minimum = minimum_list[i];
					}
				}
				int num = minimum;

				if(i == 0){
					break;
				}

				if(num == dp[i-1][j-1]){
					try{
						if(j != 0){
							str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
							str2_list.add(str2[j-1]);
							count = count--;
							i = i--;
							j = j--;
						}else if(j == 0){
							str1_list.add(str1[i-1]+" "+"({ })");
							i = i--;
						}
					}catch(Exception e){
						System.out.println("err");
					}
				}else if(num == dp[i][j-1]){
					if(j != 0){
						if(count > 0){
							count_null.add(String.valueOf(count));
						}
						count = count--;
						str2_list.add(str2[j-1]);
						j = j--;
					}else if(j == 0){
						if(count != count){
							str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
						}else{
							str1_list.add(str1[i-1]+" "+"({ })");
						}
						i = i--;
					}
				}else if(num == dp[i-1][j]){
					str1_list.add(str1[i-1]+" "+"({ })");
					i = i--;
				}
			}

			if(str2.length() < b.length()){
				List<String> str1_list = new ArrayList<String>();
				List<String> str2_list = new ArrayList<String>();
				i = str1.length();
				j = str2.length();
				int count = Math.min(i,j);
				List<int> count_null = new ArrayList<int>();
				for(int m = 1;m <= (Math.max(i,j)+8);m++){

					//caculate minumum number from dp
					int[] minimum_list = new int[3];
					minimum_list[0] = Math.min(dp[i-1][j], dp[i][j-1]);
					minimum_list[1] = Math.min(dp[i-1][j], dp[i-1][j-1]);
					minimum_list[2] = Math.min(dp[i][j-1], dp[i-1][j-1]);
					int minimum = minimum_list[0];
					for(int i = 0; i < minimum_list.length();i++){
						if(minimum > minimum_list[i]){
							minimum = minimum_list[i];
						}
					}
					int num = minimum;

					if(j == 0){
						break;
					}

					if(num == dp[i-1][j-1]){
						try{
							if(j != 0){
								str1_list.add(str1[i-1]+" "+"({ "+String.valueOf(count)+" })");
								str2_list.add(str2[j-1]);
								count = count--;
								i = i--;
								j = j--;
							}else if(j == 0){
								str1_list.add(str1[i-1]+" "+"({ })");
								i = i--;
							}
						}catch(Exception e){
							System.out.println("err");
						}
					}else if(num == dp[i][j-1]){
						if(j != 0){
							if(count > 0){
								count_null.add(String.valueOf(count));
							}
							count = count--;
							str2_list.add(str2[j-1]);
							j = j--;
						}else if(j == 0){
							if(count > 0){
								count_null.add(String.valueOf(count));
							}
							count = count--;
						}
					}else if(num == dp[i-1][j]){
						str1_list.add(str1[i-1]+" "+"({ })");
						i = i--;
					}
				}
			}
			count_null = Collections.reverse(count);
			count_null = String.join(" ",count_null)+" ";
			if(count_null.length() > 1){
				str1_list.add("NULL ({ "+String.valueOf(count_null)+"})");
			}else{
				str1_list.add("NULL ({ })");
			}
		}
		//
		str1_list = Collections.reverse(str1_list);
		str2_list = Collections.reverse(str2_list);

		return "#comment"+"\n"+String.valueOf(str2_list)+"\n"+String.valueOf(str1_list)+"\n";
	}

}