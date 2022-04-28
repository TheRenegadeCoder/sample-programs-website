# Baklava in Haskell

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Haskell
module Main where

main :: IO ()
main = putStrLn baklava

-- Create baklava where the top has 10 spaces and then 1 asterisk
baklava ::  String
baklava = baklavaGrow 10 1

-- Recursively grow the baklava until spaces <= zero
baklavaGrow :: Int -> Int -> String
baklavaGrow space asterisk
  | space <= 0 = line 0     asterisk ++ "\n" ++ baklavaShrink 1          (asterisk - 2)
  | otherwise  = line space asterisk ++ "\n" ++ baklavaGrow   (space - 1) (asterisk + 2)

-- Recursively shrink the baklava until asterisks <= zero
baklavaShrink :: Int -> Int -> String
baklavaShrink space asterisk
  | asterisk <= 1 = line space 1
  | otherwise     = line space asterisk ++ "\n" ++ baklavaShrink (space + 1) (asterisk - 2)

-- Return a single line of the baklava
line space asterisk = replicate space ' ' ++ replicate asterisk '*'

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.