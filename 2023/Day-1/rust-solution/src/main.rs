use std::fs::File;
use std::io::Read;

fn get_calibration_sum(content: &str) -> i32 {
    let mut final_total_1 = 0;
    let mut final_total_2 = 0;

    for mut line in content.lines() {
        let mut digits_1 = Vec::new();
        let mut digits_2 = Vec::new();

        for c in line.chars() {
            if c.is_digit(10){
                digits_1.push(c);
                digits_2.push(c);
            }

            let number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
            for (d, val) in number_words.iter().enumerate() {
                if line.starts_with(val) {
                    digits_2.push((d+1).to_string().chars().next().unwrap());
                }
            }
            if line.len() > 1 {
                line = &line[1..];
            }
            else {
                line = "";
            }
        }

        if !digits_1.is_empty() {
            let first_digit = digits_1[0].to_digit(10).unwrap();
            let last_digit = digits_1[digits_1.len()-1].to_digit(10).unwrap();
            let result = format!("{}{}", first_digit, last_digit);
            final_total_1 += result.parse::<i32>().unwrap();
        }

        if !digits_2.is_empty() {
            let first_digit = digits_2[0].to_digit(10).unwrap();
            let last_digit = digits_2[digits_2.len()-1].to_digit(10).unwrap();
            let result = format!("{}{}", first_digit, last_digit);
            final_total_2 += result.parse::<i32>().unwrap();
        }
    }
    println!("Final Total 1: {}", final_total_1);
    println!("Final Total 2: {}", final_total_2);

    final_total_2
}


fn main() {
    let file_path = "../input.txt";
    let mut file_contents = String::new();

    match File::open(file_path) {
        Ok(mut file) => {
            file.read_to_string(&mut file_contents).unwrap();
        }
        Err(_) => {
            println!("The file '{}' could not be found.", file_path);
            return;
        }
    }
    get_calibration_sum(&file_contents);
}
