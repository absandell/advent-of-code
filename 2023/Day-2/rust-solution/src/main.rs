use std::fs::File;
use std::io::Read;
use std::collections::HashMap;

fn get_possible_games(record: &str) -> i32 {
    let mut bag_max = HashMap::new();
    bag_max.insert("red", 12);
    bag_max.insert("green", 13);
    bag_max.insert("blue", 14);

    let mut possible_games_sum = 0;

    for game in record.lines() {
        let game_parts: Vec<&str> = game.split(":").collect();
        let game_id = game_parts[0].split_whitespace().nth(1).unwrap().parse::<i32>().unwrap();
        let mut valid_game = true;
        let rounds = game_parts[1].split(";");
        for round in rounds {
            let cubes:Vec<&str> = round.split(",").collect();
            for cube in cubes {
                let cube_parts: Vec<&str> = cube.split_whitespace().collect();
                let cube_value = cube_parts[0].parse::<i32>().unwrap();
                if cube_value > *bag_max.get(cube_parts[1]).unwrap() {
                    valid_game = false;
                    break;
                }
            }
            if !valid_game {
                break;
            }
        }
        if valid_game {
            possible_games_sum += game_id;
        }
    }
    possible_games_sum
}

fn get_min_cubes(record: &str) -> i32 {
    let mut sum_of_powers = 0;
    let mut color_count: HashMap<&str, [i32; 2]> = HashMap::new();

    for game in record.lines() {
        for color in &["red", "green", "blue"] {
            color_count.insert(color, [0,0]); // [current count] [max count]
        }
        let game_parts: Vec<&str> = game.split(":").collect();
        let rounds = game_parts[1].split(";");
        let mut power = 1;
        for round in rounds {
            for color in &["red", "green", "blue"] {
                color_count.get_mut(color).unwrap()[0] = 0; // Setting all current to 0
            }

            let cubes: Vec<&str> = round.split(",").collect();
            for cube in cubes {
                let cube_parts: Vec<&str> = cube.split_whitespace().collect();
                let count = cube_parts[0].parse::<i32>().unwrap();
                let color = cube_parts[1];
                color_count.get_mut(color).unwrap()[0] += count;
            }
            for (_, count) in color_count.iter_mut() {
                if count[0] > count[1] {
                    count[1] = count[0];
                }
            }
        }
        for count in color_count.values() {
            power *= count[1];
        }
        sum_of_powers += power;
    }
    sum_of_powers
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
    println!("{}", get_possible_games(&file_contents));
    println!("{}", get_min_cubes(&file_contents));
}
