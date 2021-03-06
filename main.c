#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<stdbool.h>

// fork n times and each thread should get a different
// consecutive number as it's return value
// the parent thread returns 0
unsigned fork_n(unsigned n){
    pid_t id = 0;
    unsigned count = 0;
    while(id == 0 && count < n){
        id = fork();
        count++;
    }
    if(id == 0){
        return 0;
    }
    return count;
}

void print_bin_string(bool* bin_string, int n){
    for(int i = 0; i < n; i++){
        // true is 1
        // false is 0
        putchar(bin_string[i] + '0');
    }
    putchar('\n');
}

bool is_numeric(char* string){
    while(*string != '\0'){
        if(*string < '0' || *string > '9'){
            return false;
        }
        string++;
    }
    return true;
}

int get_int(char* prompt){
    char* line = NULL;
    size_t cap = 0;
    while(1){
        fputs(prompt, stdout);
        if(getline(&line, &cap, stdin) == -1){
            fputs("Could not read line\n", stderr);
            exit(1);
        }
        int result;
        line[strlen(line) - 1] = '\0';
        if(sscanf(line, "%d", &result) >= 1){
            return result;
        }
        printf("\"%s\" is not a number\n", line);
    }
}

bool m_spaced(bool* bin_string, int n, int m){
    if(m > n || m < 2){
        return true;
    }
    int step_size_limit = n / m + 1;
    for(int step_size = 1; step_size <= step_size_limit; step_size++){
        int offset_limit = n - m - (m - 1) * (step_size - 1);
        for(int offset = 0; offset <= offset_limit; offset++){
            bool spaced = true;
            for(int step = 0; step < m; step++){
                int index = step * step_size + offset;
                if(!bin_string[index]) { // 0
                    spaced = false;
                    break;
                }
            }
            if(spaced){
                return true;
            }
        }
    }
    return false;
}

int count(bool* bin_string, int n, bool target){
    int count = 0;
    for(int i = 0; i < n; i++){
        if(bin_string[i] == target){
            count++;
        }
    }
    return count;
}

void print_nkm_strings(int n, int k, int m){
    bool* bin_string = malloc(sizeof(bool) * n);
    int limit = pow(2, n);
    for(int _i = 0; _i < limit; _i++){
        // do stuff with string
        if(count(bin_string, n, 1) >= k && !m_spaced(bin_string, n, m)){
            print_bin_string(bin_string, n);
        }
        // end do stuff with string
        for(int i = 0; i < n; i++){
            if(bin_string[i]){
                bin_string[i] = 0;
            }else{
                bin_string[i] = 1;
                break;
            }
        }
    }
}

int main(int argc, char** argv){
    int min_len = 28;
    int max_len = 30;
    int n, k, m;
    switch(argc){
        case 1:
        case 2:
        case 3:
            n = get_int("Enter n> ");
            k = get_int("Enter k> ");
            m = get_int("Enter m> ");
            break;
        case 4:
            n = atoi(argv[1]);
            k = atoi(argv[2]);
            m = atoi(argv[3]);
            break;
        default:
            break;
    }
    print_nkm_strings(n, k, m);
    return 0;
}
