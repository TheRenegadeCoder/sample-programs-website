---

---

Welcome to the Capitalize in Clojure page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Clojure
(ns capitalize
	(:gen-class))

(defn- is-valid-input [args]
  (and 
    (not= (count args) 0) 
    (not= (first args) "")))

(defn- print-error []
  (println "Usage: please provide a string"))

(defn- capitalize [s]
  (str 
    (clojure.string/upper-case 
      (subs s 0 1)) (subs s 1)
  ))

(defn main [args]
  (if (is-valid-input args) 
    (println (capitalize (first args)))
    (print-error)
  ))


(main *command-line-args*)

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.