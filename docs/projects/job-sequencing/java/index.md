---

title: Job Sequencing in Java
layout: default
date: 2022-04-28
last-modified: 2022-07-17

---

Welcome to the [Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

/** Invalid input exception to handle errors. */
class InvalidInputException extends Exception {}

public class JobSequencing {

    public static class Job {
        int deadline;
        int profit;

        public Job(int profit, int deadline) {
            this.profit = profit;
            this.deadline = deadline;
        }
    }

    private static List<Job> createJobList(List<Integer> deadlines, List<Integer> profits) {
        List<Job> jobs = new ArrayList<>();
        for (int i = 0; i < deadlines.size() ; i++ ) {
            jobs.add(new Job(profits.get(i), deadlines.get(i)));
        }

        return jobs;
    }

    public static class Sorted implements Comparator {

        public int compare(Object o1, Object o2) {
            Job j1 = (Job)o1;
            Job j2 = (Job)o2;

            if (j1.profit != j2.profit) {
                return j2.profit - j1.profit;
            } else {
                return j2.deadline - j1.deadline;
            }
        }
    }

    private static int getMaxProfit(List<Job> jobs, int size) {
        int maxProfit = 0;
        Sorted sorter = new Sorted();
        jobs.sort(sorter);

        TreeSet<Integer> ts = new TreeSet<>();

        for (int i = 0; i < size; i++) {
            ts.add(i);
        }

        for (int i = 0; i < size; i++) {
            Integer x = ts.floor(jobs.get(i).deadline - 1);

            if (x != null) {
                maxProfit += jobs.get(i).profit;
                ts.remove(x);
            }
        }
        return maxProfit;
    }

    private static List<Integer> converStringToList(String arg) {
        List<Integer> list = new ArrayList<>();
        if (arg.length() > 0) {
            for (String p : arg.split(",")) {
                list.add(Integer.parseInt(p.trim()));
            }
        }
        return list;
    }

    public static void main(String[] args) {

        try {
            //Check for no input and empty input and missing input
            if(args.length < 2 || "".equals(args[0]) || "".equals(args[1])) {
                throw new InvalidInputException();
            }

            List<Integer> profits = converStringToList(args[0]);
            List<Integer> deadlines = converStringToList(args[1]);

            //Check if two lists are different Lengths
            if (profits.size() != deadlines.size()) {
                throw new InvalidInputException();
            }

            List<Job> jobs = createJobList(deadlines, profits);
            System.out.println(getMaxProfit(jobs, jobs.size()));

        } catch (NumberFormatException | InvalidInputException e) {
            System.err.println("Usage: please provide a list of profits and a list of deadlines");
        }
    }

}
```

{% endraw %}

[Job Sequencing](https://sampleprograms.io/projects/job-sequencing) in [Java](https://sampleprograms.io/languages/java) was written by:

- JaneLiu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 26 2019 20:48:26. The solution was first committed on Oct 17 2019 20:32:42. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).