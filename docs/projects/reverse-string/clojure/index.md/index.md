# Reverse String in Clojure

## Solution

```Clojure
(ns reverse-string
	(:gen-class))

(defn main [s]
  (println(clojure.string/reverse s)))

(main (first *command-line-args*))
```