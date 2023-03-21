print("hello,asdsadadsadaweewwewdwdewdwdwd")
print("hello,new1")
print("hello,new2")
print("hello,new3")

public class TwoSum {
    public static void main(String[] args) {
        //初始化
        TimeMenIntervalUtil.start();

        int[] nums = {1,2,4,5,11,8,10};
        int target =12;

        //有序数组 - 方法1-双下标
        int i = 0;
        int j = nums.length -1;

        while (i<j){
            int result = nums[i] + nums[j];
            if(result == target){
                System.out.printf("%d,%d\n",nums[i],nums[j]);
                i++;
            }else if (result > target){
                j--;
            }else if (result > target){
                i++;
            }
        }
        //有序数组-方法2-pom.xml/common(支持无序)
        for (int k=0; k<nums.length-1;k++ ){
            int value = target - nums[k];
            if (ArrayUtils.contains(nums,value)){
                System.out.printf("%d,%d\n",nums[k],value);
            }
        }
        //时间和内存耗用情况
        TimeMenIntervalUtil.end();
    }
}
