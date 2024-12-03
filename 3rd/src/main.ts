import { readFileSync } from "fs";

const main = (): void => {
    const input = readFileSync("./src/input.txt", "utf-8");
    const total = getMultiplications(input);

    console.log(`Total: ${total}`);
}

const validInteger = (str: string): boolean => {
    if (str.length === 0) return false;

    // ensure all characters are digits - parseInt is not reliable for this.
    for (let char of str) {
        if (char < "0" || char > "9") return false;
    }

    return true;
}

const getMultiplications = (input: string): number => {
    let paused = false;
    let total = 0;

    const parts = input.split("mul(");

    for (let i = 1; i < parts.length; i++) {
        let part = parts[i];
        
        if (!part.includes(")")) continue;

        if (!paused) {
            const params = part.slice(0, part.indexOf(")")).split(",");
    
            if (params.length === 2 && validInteger(params[0]) && validInteger(params[1])) {
                const num1 = Number(params[0]);
                const num2 = Number(params[1]);
    
                total += num1 * num2;
            }
        }

        if (paused && part.includes("do()")) {
            paused = false;
        }

        if (!paused && part.includes("don't()")) {
            paused = true;
        }
    }

    return total;
}

main();