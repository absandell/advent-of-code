fn get_possible_games(&file_contents) -> i32 {
    let bag_max = {
        "red": 12,
        "green": 13,
        "blue": 14
    };
    let mut possible_games_sum = 0;
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
    get_possible_games(&file_contents);
}
