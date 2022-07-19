#for problemset A, B, C ... && Codechef codes for problems
function runsamples # runnig and testing sample testcases
    echo "Compiling $argv.cpp with G++17..." \n
    sleep 1
    #navigating to problem dir:
    # cd ..
    cd $argv
    # Compiling file
    g++ -std=c++17 $argv.cpp -o $argv.out
    # Running testcases:
    if test -f sample_input_1.txt;
        ./$argv.out <sample_input_1.txt> my_output_1.txt
        if cmp -s sample_output_1.txt my_output_1.txt;
            echo Running Testcase 1:(set_color --bold green) 'Passed!' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_1.txt my_output_1.txt
            echo ""
        else
            echo Running Testcase 1:(set_color --bold red) 'Failed' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_1.txt my_output_1.txt
            echo ""
        end
    end
    if test -f sample_input_2.txt;
        ./$argv.out <sample_input_2.txt> my_output_2.txt
        if cmp -s sample_output_2.txt my_output_2.txt;
            echo Running Testcase 2:(set_color --bold green) 'Passed!' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_2.txt my_output_2.txt
            echo ""
        else
            echo Running Testcase 2:(set_color --bold red) 'Failed' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_2.txt my_output_2.txt
            echo ""
        end
    end
    if test -f sample_input_3.txt;
        ./$argv.out <sample_input_3.txt> my_output_3.txt
        if cmp -s sample_output_3.txt my_output_3.txt;
            echo Running Testcase 3:(set_color --bold green) 'Passed!' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_3.txt my_output_3.txt
            echo ""
        else
            echo Running Testcase 3:(set_color --bold red) 'Failed' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_3.txt my_output_3.txt
            echo ""
        end
    end
    if test -f sample_input_4.txt;
        ./$argv.out <sample_input_4.txt> my_output_4.txt
        if cmp -s sample_output_4.txt my_output_4.txt;
            echo Running Testcase 4:(set_color --bold green) 'Passed!' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_4.txt my_output_4.txt
            echo ""
        else
            echo Running Testcase 4:(set_color --bold red) 'Failed' #(set_color normal)
            echo " Expected                              My Output"
            echo "```````````                           ````````````"
            diff -y -W 70 sample_output_4.txt my_output_4.txt
            echo ""
        end
    end

    cd ..
end

function checkfile 
    if test -f $argv;
        echo (set_color --bold green)"File Exist."
    else
        echo (set_color --bold red)"File Doesn't Exist."
    end
end
