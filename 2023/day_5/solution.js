const fs = require('fs');

function readFile(path = "input.txt") {
    const fileContent = fs.readFileSync(path, 'utf-8');
    return fileContent.split('\n').map(line => line.trim());
}

function getSeeds(input) {
    return input[0].split(":")[1].split(/\s+/);
}

function getMaps(input) {
    const maps = [];
    const mapInput = input.slice(2);
    let currentMap = [];

    for (const line of mapInput) {
        if (line === "") {
            maps.push([...currentMap]);
            currentMap = [];
        } else {
            currentMap.push(line);
        }
    }

    if (currentMap.length > 0) {
        maps.push([...currentMap]);
    }

    return maps;
}

function createConversionDictionary(map) {
    const mapping = {};
    let destinationRange, sourceRange, rangeLength, source, destination;

    for (let i = 1; i < map.length; i++) {
        [destinationRange, sourceRange, rangeLength] = convertLine(map[i]);

        for (let j = 0; j < rangeLength; j++) {
            source = sourceRange + j;
            destination = destinationRange + j;

            // Only store mappings if source and destination are different
            if (source !== destination) {
                mapping[source] = destination;
            }
        }
    }
    return mapping;
}

function convertLine(line) {
    const [destinationRange, sourceRange, rangeLength] = line.split(/\s+/).map(Number);
    return [destinationRange, sourceRange, rangeLength];
}

function runTheConversion(seed, mapArr) {
    let changingSeed = seed;
    for (const mapping of mapArr) {
        changingSeed = mapping[changingSeed] || changingSeed;
    }
    return changingSeed;
}

function solvePart1() {
    console.log("solving");
    const inputData = readFile();
    const seeds = getSeeds(inputData);
    const maps = getMaps(inputData);

    const conversionMapArr = maps.map(createConversionDictionary);

    const locationNums = seeds.map(seed => runTheConversion(parseInt(seed), conversionMapArr));

    console.log("min:", Math.min(...locationNums));
}

solvePart1();