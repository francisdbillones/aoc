import Data.Char (digitToInt, isDigit)

digitWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

isDigitWord :: String -> Int -> Bool
isDigitWord s i = any (\word -> take (length word) (drop i s) == word) digitWords

findDigitOrDigitWord f s =
  let go i = isDigit (s !! i) || isDigitWord s i
   in if any go [0 .. (length s - 1)]
        then Just (f (filter go [0 .. (length s - 1)]))
        else Nothing

getDigitWord s i = fst (head (filter snd (map (\k -> let word = digitWords !! k in (k, word == take (length word) (drop i s))) [0 .. (length digitWords)])))

getDigitOrDigitWord s i
  | isDigit (s !! i) = Just (digitToInt (s !! i))
  | isDigitWord s i = Just (getDigitWord s i)

main = do
  contents <- readFile "input.txt"
  let myLines = lines contents

  let my_func s =
        do
          first_i <- findDigitOrDigitWord head s
          last_i <- findDigitOrDigitWord last s
          first_digit <- getDigitOrDigitWord s first_i
          last_digit <- getDigitOrDigitWord s last_i
          return $ first_digit * 10 + last_digit

  print $ sum $ map (maybe 0 id . my_func) myLines