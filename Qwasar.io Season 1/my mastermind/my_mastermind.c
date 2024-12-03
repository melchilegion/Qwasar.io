#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define NUM_PIECES 9
#define CODE_LENGTH 4
#define MAX_ATTEMPTS 10

char pieces[NUM_PIECES] = {'0', '1', '2', '3', '4', '5', '6', '7', '8'};
char code[CODE_LENGTH];
int attempts;

void generate_code() {
    srand(time(NULL));
    for (int i = 0; i < CODE_LENGTH; i++) {
        code[i] = pieces[rand() % NUM_PIECES];
    }
}

void print_code(char *code) {
    for (int i = 0; i < CODE_LENGTH; i++) {
        printf("%c", code[i]);
    }
    printf("\n");
}

int count_well_placed(char *guess) {
    int count = 0;
    for (int i = 0; i < CODE_LENGTH; i++) {
        if (guess[i] == code[i]) {
            count++;
        }
    }
    return count;
}

int count_misplaced(char *guess) {
    int count = 0;
    for (int i = 0; i < CODE_LENGTH; i++) {
        for (int j = 0; j < CODE_LENGTH; j++) {
            if (i!= j && guess[i] == code[j]) {
                count++;
                break;
            }
        }
    }
    return count;
}

void game_play() {
    char guess_it[CODE_LENGTH + 1]; int round = 0;
    attempts = MAX_ATTEMPTS; // initialize attempts here
    while (round < attempts) {
        printf("--- Round %d ---\n> ", round);
        int i = 0; char c;
        while (read(0, &c, 1) > 0 && c!= '\n') {
            if (i < CODE_LENGTH) guess_it[i++] = c;}
        if (i == 0) {
            printf("Game stopped!\n");
            return;}
        guess_it[i] = '\0'; int valid = 1;
        for (int j = 0; j < CODE_LENGTH; j++)
            if (!strchr("012345678", guess_it[j])) valid = 0;
        if (!valid || strlen(guess_it)!= CODE_LENGTH) {
            printf("Wrong input!\n"); continue;}
        int well_placed = count_well_placed(guess_it), misplaced = count_misplaced(guess_it);
        printf("Well placed pieces: %d\nMisplaced pieces: %d\n", well_placed, misplaced);
        if (well_placed == CODE_LENGTH) {
            printf("Congratz! You did it!\n");
            return;}
        round++;}
    printf("You didn't find the secret code!\n");}

int main(int argc, char **argv) {
    if (argc > 1 && strcmp(argv[1], "-c") == 0) {
        if (strlen(argv[2])!= CODE_LENGTH) {
            printf("Invalid code length\n");
            return 1;
        }
        for (int i = 0; i < CODE_LENGTH; i++) {
            if (!strchr("012345678", argv[2][i])) {
                printf("Invalid piece\n");
                return 1;
            }
        }
        strcpy(code, argv[2]);
    } else {
        generate_code();
    }
    if (argc > 3 && strcmp(argv[3], "-t") == 0) {
        attempts = atoi(argv[4]);
    } else {
        attempts = MAX_ATTEMPTS;
    }
    printf("Will you find the secret code?\nPlease enter a valid guess\n");
    game_play();
    return 0;
}