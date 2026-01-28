- [React](#react)
  - [React Crash Course - Day 1](#react-crash-course---day-1)
  - [React Crash Course - Day 2](#react-crash-course---day-2)
    - [React 18 StrictMode (Dev)](#react-18-strictmode-dev)
    - [useState](#usestate)
    - [useEffect(\[\])](#useeffect)
    - [useEffect cleanup](#useeffect-cleanup)
    - [installHook.js](#installhookjs)
    - [Summary](#summary)
  - [React Crash Course - Day 3 RTK Query, Async Data, and Server State](#react-crash-course---day-3-rtk-query-async-data-and-server-state)
    - [1. the Big mental shift](#1-the-big-mental-shift)
    - [2. Server State vs UI State (critical distinction)](#2-server-state-vs-ui-state-critical-distinction)
    - [3. What `useGetTodosQuery()` really is](#3-what-usegettodosquery-really-is)
    - [4. Where the HTTP request actually happens](#4-where-the-http-request-actually-happens)
    - [5. How to navigate to source code in `node_modules`](#5-how-to-navigate-to-source-code-in-node_modules)
    - [6. Cache, Tags, and invalidatesTags](#6-cache-tags-and-invalidatestags)
    - [8. onQueryStarted — the missing piece](#8-onquerystarted--the-missing-piece)
    - [9. Optimistic Update Pattern (core pattern)](#9-optimistic-update-pattern-core-pattern)
    - [Summary](#summary-1)
  - [Day 3.5: Redux + RTK Query - Key takeaways (Day 3 Final)](#day-35-redux--rtk-query---key-takeaways-day-3-final)
    - [1️⃣ What the Redux Store Really Is](#1️⃣-what-the-redux-store-really-is)
    - [2️⃣ Two Kinds of State (this is the BIG idea)](#2️⃣-two-kinds-of-state-this-is-the-big-idea)
      - [A) UI / Client State (your responsibility)](#a-ui--client-state-your-responsibility)
      - [B) Server / Remote State (RTK Query’s responsibility)](#b-server--remote-state-rtk-querys-responsibility)
    - [3️⃣ Why RTK Query Has a Reducer (important insight)](#3️⃣-why-rtk-query-has-a-reducer-important-insight)
    - [4️⃣ What `configureStore` Is Wiring Together](#4️⃣-what-configurestore-is-wiring-together)
    - [5️⃣ Why `[todoApi.reducerPath]` Looks Weird](#5️⃣-why-todoapireducerpath-looks-weird)
    - [6️⃣ Typed Hooks = Less TypeScript Pain](#6️⃣-typed-hooks--less-typescript-pain)
    - [7️⃣ Why UI State Moved Out of `App.tsx`](#7️⃣-why-ui-state-moved-out-of-apptsx)
    - [8️⃣ Correct Mental Model Going Forward](#8️⃣-correct-mental-model-going-forward)
    - [9️⃣ Rule of Thumb (write this down)](#9️⃣-rule-of-thumb-write-this-down)
  - [React JS/TS phase 1](#react-jsts-phase-1)
    - [Day 1](#day-1)
    - [Day 2](#day-2)
    - [Day 3](#day-3)
    - [Day 4](#day-4)
    - [Takeaway / my own conceptual question](#takeaway--my-own-conceptual-question)
    - [Day 5](#day-5)
    - [Summary](#summary-2)
  - [React JS/TS phase 2](#react-jsts-phase-2)
    - [Session 1 - “JS runtime mental model” for React devs](#session-1---js-runtime-mental-model-for-react-devs)
    - [Session 2 - Closures + “why React doesn’t update closure”](#session-2---closures--why-react-doesnt-update-closure)
    - [Session 3 - Arrow functions, `this`, and event handlers](#session-3---arrow-functions-this-and-event-handlers)
    - [Session 4 TypeScript for React (props, callbacks, hooks)](#session-4-typescript-for-react-props-callbacks-hooks)
    - [Session 5 useMemo, React.memo, and React Performance Myths](#session-5-usememo-reactmemo-and-react-performance-myths)
    - [Session 6 - Effects](#session-6---effects)
  - [React Redux phase 3](#react-redux-phase-3)
    - [3.1 Redux without React](#31-redux-without-react)
  - [React, Javascripts Fundamentals](#react-javascripts-fundamentals)


# React

## React Crash Course - Day 1

- 1️⃣ Modern Frontend Mental Model
  - Frontend ≠ Backend
  - Frontend code runs:
    - in the browser
    - over the network
    - with security restrictions (CORS)
  - Therefore it needs:
    - a **dev server**
    - a **bundler**
  - fast feedback loops (**HMR**)
- 2️⃣ What Vite Actually Does
  - **Dev Server**
    - serves ES modules over HTTP
    - transforms TS / JSX on the fly
  - **HMR(Hot module Replacement)**
    - updates changed modules only
    - avoids full page reload
  - **Production bundling**
    - outputs static assets(`dist/`)
    - optimized for browser delivery
  - 👉 Browser cannot run TS / JSX directly.
- 3️⃣ React Rendering Model
  - Core rule: React re-renders UI from **state**, not from manual DOM updates
  - `setState -> re-render`
  - Component function runs again
  - JSX describe what UI should look like
- 4️⃣ State & Controlled Inputs
  
  **Controlled Input Pattern**
  ```jsx
    const [value, setValue] = useState("");

    <input value={value} onChange={e => setValue(e.target.value)} />
  ```
  - React is the **single source of truth**
  - Input value always reflects state
  - Enables validation, formatting, disabling, etc.
- 5️⃣ Derived State:
  - Derived state = computed from other state.
  - `const remaining = todos.filter(t => !t.done).length;`
  - Rules:
    - Do not store it
    - Compute it from existing state
- 6️⃣ `useEffect` - **Side Effects**
  - `useEffect` is for:
    - DOM effects (`document.title`)
    - data fencing
    - timers / subscriptions
    - syncing external systems
  - Key properties:
    - runs after render
    - re-runs when dependencies change
    - NOT a constructor
    - NOT backend “initialization”
- 7️⃣ useMemo — Cache, Not Optimizatio
  - What useMemo actually does
    - Caches a computed value
    - Returns cached value only if dependencies are === equal
  - Important Insight
    - useMemo can be more expensive than recomputing.
    - Why:
      - dependency comparison cost
      - cache bookkeeping
      - often recomputes anyway if deps change frequently
  - Rule of Thumb
    - Use useMemo only if:
      - computation is expensive
      - dependencies change rarely
      - referential stability matters
    - Otherwise: recompute.
- 8️⃣ Fake Backend Call Pattern

  **Frontend async pattern:**
  ```jsx
    setLoading(true);
    try {
      const data = await fetchStuff();
      setState(data);
    } finally {
      setLoading(false);
    }
  ```
  Key idea:
  - Async logic lives in event handlers or effects
  - Loading & error are explicit UI states

- 9️⃣ CORS (Browser Security)
  - Different origin = protocol + host + port
  - Browser blocks cross-origin reads by default
  - Server must explicitly allow via CORS headers
  
  This is enforced by the browser, not the server.

- 🔑 Day 1 Core Takeaways
  - React is a **state** -> **render** -> **effect** machine
  - Dev servers exist because browsers can't compile modern frontend code
  - Hooks are **not magic** -- the are discplined APIs around render cycles
  - `useMemo` is a cache invalidation tool, not a performance gurantee. 

## React Crash Course - Day 2

### React 18 StrictMode (Dev)

- React intentionally mounts components twice in dev
- Sequence: mount → unmount → mount
- Purpose: detect unsafe side effects
- Happens ONLY in development
- Production runs mount once

### useState
- Holds component-local state
- setState triggers re-render
- Never mutate directly

### useEffect([])

- NOT guaranteed to run once in dev
- MUST be idempotent
- Cleanup must fully undo side effects

### useEffect cleanup
 
- useEffect may run multiple times
- Returned function by useEffect is the cleanup
  ```js
    useEffect(() => {
      window.addEventListener("resize", handler);
      return () => window.removeEventListener("resize", handler);
    }, []);
  ```
- Cleanup runs:
  - on unmount
  - before effect re-runs
  - in React 18 StrictMode (dev)
- Always clean:
  - event listeners
  - timers
  - subscriptions
  - observers

### installHook.js

- Injected by React DevTools
- Used for inspection & profiling
- Not part of app code

### Summary

- ✅ Triggers: What triggers Re-render
  - `setState`
  - parent re-render
  - props change
  - context change
- ❌ Does NOT trigger:
  - local variable mutation
  - `useRef.current` change
  - `console.log`
- `useState` what it really does
  - `useState` is how `React` remembers values aross reners
  - calling `setState` schedules a re-render
  - State updates are **batched & async**
  - State mustg be treated as **immutable**

## React Crash Course - Day 3 RTK Query, Async Data, and Server State

### 1. the Big mental shift
**old mindset**: (local state / thunks/ fake fetch)
> "I call an API, wait for it, then put the result into state."

**New mindset**: (RTK query)
> My component declares a dependency on server data.
Fetching, caching refetching and lifecycle are handled by RTK Query.

### 2. Server State vs UI State (critical distinction)

- Server State (RTK Query owns this)
  - Data that comes from the backend
  - Can be refetched at any time
  - Shared across components
  - Cached globally

  Examples
  - `todos`
  - `users`
  - `orders`

  Managed by RTK Query

- UI / Client State (React/slices own this)
  - Input fields
  - Modal open/close
  - Filters, tabs
  - Temp UI-only values
  
  Examples:
  - `text` input
  - `selectedTab`
  - `isDialogOpen`
  
  Managed by `useState` or **Redux slices**

### 3. What `useGetTodosQuery()` really is

```js
const { data, isLoading, error } = useGetTodosQuery();

```
This is **not**:
- a function that “calls fetch”
- an async function
- a blocking operation

This is:
- a subscription to cached server data
- a declarative statement: “This component depends on getTodos.”

RTK Query:
- checks cache
- decides whether to fetch
- updates Redux state
- triggers re-renders

### 4. Where the HTTP request actually happens

Important realization:
- The hook does NOT send HTTP requests.

The request is sent by:
- RTK Query middleware
- via fetchBaseQuery
- using the browser fetch()

Execution path (simplified):
```
useGetTodosQuery()
 → dispatch(initiate)
 → RTK Query middleware
 → baseQuery
 → fetch()

```

### 5. How to navigate to source code in `node_modules`

- Navigate to the expression
- do `ctrl` + `shift` + `p` -> **TypeScript: Go To Source Definition**

Types describe what is allowed.
Source code shows what actually happens.


### 6. Cache, Tags, and invalidatesTags

What providesTags does
```
providesTags: ["Todos"]

```
It labels cached query results:
```
getTodos → tagged as "Todos"

```

**What `invalidatesTags` does**
```
invalidatesTags: ["Todos"]

```
After a mutation succeeds:
- Mark all "Todos" cache entries as stale
- If there are active subscribers → refetch
- Important:
  ❌ It does NOT update cache
  ❌ It does NOT merge data
  ❌ It does NOT add/remove items

It only says:
**“This data might be outdated — refetch it.”**

### 8. onQueryStarted — the missing piece

What it is
- onQueryStarted is a lifecycle hook that runs:
- immediately when a mutation starts
- before the HTTP request finishes

It gives you access to:
- dispatch
- queryFulfilled (a Promise)
- the mutation arguments

What it enables
- ✅ Optimistic UI
- ✅ Direct cache updates
- ✅ Rollback on failure

This is where you can say:

“I know how to update the cache right now.”

### 9. Optimistic Update Pattern (core pattern)

Used for add, toggle, delete.

General structure:

```js
async onQueryStarted(arg, { dispatch, queryFulfilled }) {
  const patch = dispatch(
    api.util.updateQueryData("getTodos", undefined, (draft) => {
      // optimistic change
    })
  );

  try {
    await queryFulfilled;
  } catch {
    patch.undo(); // rollback
  }
}

```
Backend analogy:

`Modify in-memory cache → async DB write → rollback on exception`

### Summary

**RTK Query cache is Redux state**
Hooks are just subscriptions
Middleware performs the side effects


## Day 3.5: Redux + RTK Query - Key takeaways (Day 3 Final)

### 1️⃣ What the Redux Store Really Is

The **Redux store** is:

* A **single global state container**
* Plus the **logic that updates it**
* Plus **middleware** that handles async work

It wires together:

* UI state (your own slices)
* Server state (RTK Query)
* Async side effects (API calls)

> Think: **store = state + reducers + middleware**

---

### 2️⃣ Two Kinds of State (this is the BIG idea)

#### A) UI / Client State (your responsibility)

Stored in **Redux slices** (`createSlice`):

* Filters
* Toggles
* Selected rows
* Editing state
* Dialog open/close
* View modes

Example (`uiSlice`):

```ts
state.ui = {
  showCompleted: boolean,
  filterText: string,
  editingTodoId: string | null
}
```

Owned by:

* `uiSlice.ts`
* Updated via `dispatch(...)`

---

#### B) Server / Remote State (RTK Query’s responsibility)

Stored automatically by **RTK Query**:

* Fetched data
* Loading flags
* Error states
* Cache metadata

Example:

```ts
state.todoApi = {
  queries: {...},
  mutations: {...},
  subscriptions: {...}
}
```

Owned by:

* `todoApi.ts`
* Managed for you

> ❗ You do NOT create reducers for server data manually unless you have a special reason.

---

### 3️⃣ Why RTK Query Has a Reducer (important insight)

RTK Query:

* Is NOT just a “fetch wrapper”
* It is a **server-state manager**

It needs a reducer because it stores:

* Cached API responses
* Which queries are active
* Loading/error status
* Cache invalidation info

That’s why this exists:

```ts
[todoApi.reducerPath]: todoApi.reducer
```

Which becomes:

```ts
state.todoApi
```

---

### 4️⃣ What `configureStore` Is Wiring Together

```ts
configureStore({
  reducer: {
    ui: uiReducer,
    todoApi: todoApi.reducer,
  },
  middleware: getDefaultMiddleware => 
    getDefaultMiddleware().concat(todoApi.middleware)
})
```

This wires:

* UI state updates
* Server cache updates
* API calls & side effects
* Redux DevTools
* Type inference

---

### 5️⃣ Why `[todoApi.reducerPath]` Looks Weird

This is **computed property syntax** in JS.

```ts
[todoApi.reducerPath]: todoApi.reducer
```

Means:

```ts
"todoApi": todoApi.reducer
```

RTK Query does this so:

* You don’t typo the key
* Multiple APIs can coexist safely

---

### 6️⃣ Typed Hooks = Less TypeScript Pain

Instead of:

```ts
useDispatch()
useSelector(...)
```

We create:

```ts
useAppDispatch()
useAppSelector()
```

So:

* `dispatch` knows valid actions
* `state` knows full shape (`RootState`)
* No `any`
* Cleaner components

---

### 7️⃣ Why UI State Moved Out of `App.tsx`

We moved **filter + showCompleted** into Redux because:

* They are **app-level UI state**
* Multiple components may need them later
* They should persist across re-renders
* They should not depend on server calls

What stayed local:

* “Add todo” input text (`useState`)

  * temporary
  * component-scoped
  * not shared

---

### 8️⃣ Correct Mental Model Going Forward

```
┌──────────────┐
│   React UI   │
└──────┬───────┘
       │
useSelector / useDispatch
       │
┌──────▼────────────────┐
│     Redux Store        │
│                        │
│  uiSlice               │ ← UI state
│  todoApi (RTK Query)   │ ← Server cache
│                        │
│  middleware             │ ← API calls
└────────────────────────┘
```

---

### 9️⃣ Rule of Thumb (write this down)

* **Server data?** → RTK Query
* **UI behavior?** → Redux slice
* **Temporary input?** → `useState`
* **Async logic?** → RTK Query middleware

---

## React JS/TS phase 1

### Day 1

1. A render happens when React schedules UI evaluation
   (mount, state change, parent render, StrictMode, retries).

2. Logging does not cause a render; it only observes that React ran render.

3. Logging inside render is misleading because render may run
   without any state change, user action, or DOM commit.

**Local variables die every render. State does not**

**Preparation**

```
npm create vite@latest my-app -- --template react-ts
```

### Day 2

1. What will local log on each click?
> 1

2. What will count log on each click?
> count + 1; 

3. Will either ever increase beyond 1?
> local will stay at 1; whereas count can go beyond 1

**Takeaway**
- If multiple state updates happen before the next render, setCount(count + 1) can lose updates.
- The functional form setCount(c => c + 1) won’t.
- Because count is a snapshot of react state.

### Day 3

**Predications**
- if I have pressed `+` 5 times, count will be 4
- Log Later however will give me 0, because it is the snapshot it sees. 

**Practical** 3
- How do you know cleanup runs? are you telling me React clears Interval?

✍️ **End-of-Day 3 notes (must answer)**

In your own words:

- **Why did logLater see an old value?**
   - Because the the `closure` `loglater` only remebers a snapshot of the count **at that moment**
   - A closure captures values from the render that created it, not a live reference.

- **Why doesn’t React “update” closures?**
  - Because JS owns closure, not react
  - JS creates closure when doing `App()`
    - Each render = a fresh function invocation
    - Each invocation creates a new closure environment
  - React 18 is concurrent; so if closure is mutatable then it will be chaos, which closure do I choose to run? which closure do I trust?
    - If closures were mutable:
      - Which render’s closure should be updated?
      - What if React abandons a render halfway?
      - What if two renders are in flight?
    - Immutable snapshots are what make:
      - concurrent rendering
      - interruption
      - retry
      - time slicing
      
      possible at all.

   “Just like Java lambda capturing effectively final variables”

   React relies on immutable closures to make concurrency safe.

- **What does a dependency array actually control?**
  - It controls whether we should re-run the useEffect; if any one from the dep list changes, we re-run;
  - **more precisely, The** dependency array controls when React must discard the old closure and create a new one for the effect.
  - So instead of thinking "should the effect run" , think "is this closure still valid for the current render?"

- **Why does the functional updater solve many closure bugs?**
  - The functional updater does not close over state. React calls it later and passes in the latest committed state.
  - That’s why it behaves like:
    - CAS
    - Atomic update
    - reducer logic

### Day 4

✍️ **End-of-Day 4 questions (answer in your own words)**

- **When does useEffect run relative to render**?
  - useEffect runs after every render
  - **more precisely** useEffect runs after React commits the render to the DOM, not merely after the render function is called.
  - React may call render and discard it
  - Effects only run for committed renders

- **When does cleanup run?**
  - Cleanup runs before the **next effect** is executed, or when the component unmounts.
  - A render can happen without an effect re-running
  - Cleanup is tied to effect re-execution, not render itself

- **What does the dependency array actually mean?**
  - Dependency array controls, when we should discuss the old closure, and create a new one

- **Why does StrictMode run effects twice in dev?**
  - In dev mode, react will try to check if the effect run can be successfully cleaned; that is why it run twice to observe the cleanup.

- **Why must effects be idempotent?**
  - if it is not, the previous closure will have impacts on the current closure
  - then result becomes unpredictable
  - in React 18 we have concurrency; if multiple effect runs simultaneously, there will be race conditions.
  - From ChatGPT words: Effects must be idempotent because React may:
    - run them more than once (*ticks* example)
    - interrupt them
    - clean them up and restart them
    - retry renders in concurrent mode
  - If an effect assumes “run exactly once”, it’s broken by design.

### Takeaway / my own conceptual question

1️⃣ **What does “React commits changes to the DOM” actually mean?**

> “Commit” has nothing to do with compiling TypeScript or generating HTML strings.
It is a runtime phase where React mutates the browser DOM to match a computed UI tree.

- Step 0 — **TypeScript / JSX (build time, not runtime)**
    First, **my code**
    ```js
        function App() {
        return <div>Hello</div>;
        }
    ```
    Then, is compiled (by Vite / Babel / TS) into somethin like:
    ```js
    function App() {
        return React.createElement("div", null, "Hello");
    }
    ```
    That’s it.

    ❌ No HTML generation

    ❌ No DOM touching

    ✅ Just JavaScript functions

    This is build-time, not what we mean by “commit”.

- Step 1 - **Render phase** (pur computation, no DOM)
  - At runtime, React does this:
  ```
      call App()
      → returns a tree of React elements (plain JS objects)
  ```

  Example (conceptually)
  ```
  {
      type: "div",
      props: { children: "Hello" }
  }

  ```
  - **Important properties of the render phase:**
      - ✅ Pure computation
      - ✅ No DOM access
      - ✅ No side effects
      - ❌ Nothing visible changes yet
      - ❌ Browser is not touched
  - This is where:
      - React may run your component multiple times
      - React may abandon work
      - React may retry
      - React may pause (React 18)
  - This phase is interruptible.

- Step 2 — **Reconciliation** (still no DOM)
  - React now compares:
  ```
      previous UI tree
      vs
      new UI tree
  ```

  - it calculates:
      - What node changed
      - what stayed the same
      - what must be inserted /updated/removed
  - This produces a **mutation plan**, no DOM changes yet

  Still

  ❌ No DOM mutation

  ❌ No layout

  ❌ No paint
    
- Step 3 — **Commit phase (THIS is the key)**
  - Now react enters the commit phase
  - This is when Reacrt actually:
      - calls `document.createElement`
      - Sets attribute
      - updates text nodes
      - Attaches event listeners
      - Remove nodes
      - Runs `useLayoutEffect`
      - Then schedules `useEffect`
  - **This is the moment the browser DOM is mutated**
  - Key properties 
  - ✅ DOM mutations happen
  - ✅ Effects are scheduled
  - ❌ Cannot be interrupted
  - ❌ Must be fast
  - ❌ Must be consistent
  - This is why Reacts separates
  - render (pure, retryable)
  - commit (imperative, one-shot)

  When I said:

  > “useEffect runs after React commits the render”

  I meant:

  > After the DOM actually reflects the new UI

  > After the browser has something concrete to show

  > After React knows this render “won”

  This is conceptually similar to

  > database transaction planning

  > write-ahead log

  > then commit changes

  Hence the word commit.

2️⃣ **JavaScript, threads, and “concurrency” in React 18**

- **Is Javacsript single-threaded**
  
  **Yes, mostly**
  ```
  JavaScript execution (your JS code) runs on one main thread.
  No shared-memory multithreading
  No data races like Java threads
  No locks / volatile / CAS in user JS
  ```

- **Does Javascript have a GIL like Python?**
  
  **No, and this is important**

  Python’s GIL exists because:
  - Multiple OS threads execute Python bytecode
  - The GIL serializes them

  JavaScript is different:
  - There is only one execution thread
  - No need for a GIL
  - The event loop controls scheduling

  So JS ≠ Python threading model.

- **Then what does concurrency mean in React 18?**
  
  React 18 concurrency = cooperative scheduling
  ```
    React render work
    → pause
    → browser handles input / paint
    → resume render
  ```
  This is not multithreading

  It is closer to:
  cooperative multitasking, co-routines, fibers (literally)

- **Why closure must be immutable (connecting back to Day 3)**
  
  Because React can:
  ```
  Start rendering version A
  Pause it
  Start rendering version B
  Discard A
  Commit B
  ```

  If closures were mutable:

  Which render’s closure do you mutate?

  What if render A resumes after B commits?

  **Total chaos**

  So React’s concurrency model depends on immutable snapshots.

  | Java              | React 18            |
  | ----------------- | ------------------- |
  | Threads           | Tasks               |
  | Preemptive        | Cooperative         |
  | Locks             | Immutable snapshots |
  | CAS               | Functional updates  |
  | Memory visibility | Closure snapshots   |

### Day 5

✍️ **End-of-Day 5 questions (answer these)**

- **Why do children re-render when parents render**?
  
  Children re-render when parents render because React evaluates the component tree top-down, and invoking a parent component requires invoking its children to compute the UI. Props are only used to skip re-renders when memoization (`React.memo`) is explicitly enabled.
  

- **Why does a new function cause re-render even if logic is identical**?
  
  Because a new function is a new identity; just like if I do `new Foo()` in Java; the logic in `Foo` never changes, but there is a new instance created in heap;

- **What problem do useCallback and useMemo actually solve?**
  
  `useCallback` / `useMemo` preserve reference identity across renders so that downstream consumers see the same object/function instead of a new one;
  They **cache the value**, **return the smae refernce** across renders, **until DEPENDENCIES change**; nothing is wrapped, nothing is proxied, nothing is intercepted. 
  
- **When should you not use them?**
  
  You should NOT use them when:
  - e-render cost is trivial
  - Identity stability is not observed by anyone
  - You want fresh objects to signal changes
  - Memoization adds complexity without benefit
  - A key idea:
  
  Re-rendering is not a bug. Unnecessary re-rendering is.

### Summary

By default, when a parent component renders, all its children are re-rendered,
regardless of whether props changed.

A child only skips re-rendering when React.memo is used AND all props have the
same reference identity.

New functions and objects cause re-renders because React compares props using
reference equality (===), not behavior or deep equality.

useCallback and useMemo preserve reference identity across renders by caching
values until dependencies change; they do not wrap or proxy values.

They should only be used when reference stability is observed by memoized
children or dependency arrays; otherwise they add unnecessary complexity.

Memoization is like caching:
- Caching has a lookup cost
- Caching adds invalidation complexity
- Caching is only worth it when it avoids something more expensive than itself



---
## React JS/TS phase 2

### Session 1 - “JS runtime mental model” for React devs

- React decides whether something "changed mostly by reference identity(same object/function reference vs a new one)
- `{...obj}` / `[...arr]`  only clones 1 level; nested objects are still shared references.
- "Immutable updates" means create new objects / arrays instead of mutating existing ones. 
- In React, “changed” almost always means “new reference”, not “different value”.

### Session 2 - Closures + “why React doesn’t update closure”

- Close captures the variable from the execution context where the function was created,
- Why “stale closure” happens:
  ```js
    useEffect(() => {
      console.log(count);
    }, []);
  ```
  - Effect runs once
  - Closure captures count from first render
  - Never recreated → always logs initial value

- Three solutions:
  - Dependency array (declarative)
    ```js
      useEffect(() => {
        console.log(count);
      }, [count]);
    ```
  - Functional updater (preferred for state changes)
    ```js
      setCount(c => c + 1);
    ```

  - `useRef` (imperative escape hatch)

    | Aspect           | `useState`          | `useRef`                  |
    | ---------------- | ------------------- | ------------------------- |
    | Causes re-render | ✅ Yes               | ❌ No                      |
    | Immutable        | ✅ Yes               | ❌ No                      |
    | Lifetime         | Per render snapshot | Component lifetime        |
    | Purpose          | UI / declarative    | Imperative / escape hatch |


- `useRef` is a stable object whose `.current` can mutate without causing a re-render. 
  - Java analogy:
    ```java
      class MyComponent {
        static AtomicInteger ref = new AtomicInteger();

    ```
  - it is render escap hatch
    ```js
      useEffect(() => {
        setInterval(() => {
          console.log(countRef.current); // setInterval will always read latest value from countRef
        }, 1000);
      }, []);
    ```
  - if the value affects rendering, should cause UI updates, is part of declarative sate; then ref is the **wrong** tool
  - it is perfect for:
    - timers
    - sockets
    - event listeners
    - animation loops
    - async callbacks
    - debouncing / throttling
    - imperative libraries
  - Use ref is like a handler field in Netty
      ```java
        class MyHandler extends ChannelInboundHandlerAdapter {

            private int counter; // field === useRef

            @Override
            public void channelRead(ChannelHandlerContext ctx, Object msg) {
                counter++;
                doSomethingAsync(() -> {
                    System.out.println(counter); // java will always pass the field, not the stack value
                });
            }
        }
      ```
- React state is like method-local variables recreated per event. Refs are like handler fields living for the lifetime of the component.

**Summary**:
- State is replaced per render
- Refs are shared across renders
- Closures freeze values, not refs.
- if changing a vluae should update the UI -> state
- if not -> ref

---
### Session 3 - Arrow functions, `this`, and event handlers

- Mental model
  - Inline arrow functions are fine
  - Identity changes cause re-renders
  - `useCallback` only matters when identity matters

- **Why is this usually fine?**

  ```js
  <button onClick={() => setOpen(true)} />
  ```

  this arrow function is cheap; The component is already re-rendering anayway; No memoized child depends on this function's identity.

  📌 Important nuance
  It’s not that the arrow function causes a re-render — the render already happened.
  The arrow function is just created during render.

  > **So the cost is allocation, not re-render**.

  That’s why React docs say:

  > “Premature memoization is usually unnecessary.”

- **Why is this sometimes bad?**

  ```js
  <MemoChild onClick={() => doSomething()} />
  ```

  - `React.memo` does shallow prop comparison
  - New arrow function -> new reference
  - `prevProps.onClick !== nextProps.onClick`
  - Memo short-circuits -> ❌
  - Child re-renders anyway

  If the child’s rendering does not logically depend on a new function identity, then we should use `useCallback`

**Summary**

- 1️⃣ this problems were a class-component issue
  - Methods lose this when passed as callbacks
  - `.bind(this)` or arrow functions were required

- 2️⃣ Function components avoid this entirely
  - State is captured via closures
  - No binding needed
  - One whole class of bugs disappears
- 3️⃣ Inline arrow functions
  - `onClick={() => doSomething()}`
  - New function every render
  - New identity
  - Closes over latest state
  - Usually fine, **Can defeat memoization**
- 4️⃣ Identity is the real issue
  - React compares references, not logic
  - New function reference ≠ previous one
  - Memoized children re-render
- 5️⃣ useCallback purpose
  ```js
    const handler = useCallback(() => {
      setCount(c => c + 1);
    }, []);
  ```
  - Stabilizes function identity
  - Does not optimize logic
  - Only useful when identity matters
- 6️⃣ Avoid stale closures
  - Prefer functional updaters
  - Or include dependencies
  - Or read mutable values from refs
- 7️⃣ Golden rules
  - Inline arrows are fine unless identity matters.
  - useCallback is for memoized children and prop stability.
  - Never memoize “just in case”.

### Session 4 TypeScript for React (props, callbacks, hooks)

- 1️⃣**Why is this bad ?**
  ```ts
  const [state, setState] = useState(null);

  ```
  if you do this, it will be inferred that `state` has null type forever. correct fix: `useState<T | null>(null);`

- 2️⃣ **Why is this better than inline arrow**?
  ```ts
    const onToggle = useCallback((id: string) => {
      ...
    }, []);

  ```
  `useCallback` ensures the same function reference is reused across renders, avoiding unnecessary function re-creation and preventing memozied children from re-rendering due to identity changes.
  Allocation cost is tiny; avoiding useless child renders is the big gain.


- 3️⃣ **When should you explicitly type useState<T>()**?
  - Initial value is `null` or `undefined`
  - Initial value is an empty array or object
  - State is a union type
  - You want to constrain future assignments
  - Example
    ```ts
      useState<Todo | null>(null);
      useState<Todo[]>([]);
      useState<"idle" | "loading" | "error">("idle");
    ```

**Summary**

- 1️⃣ Props typing
  - Always define explicit prop types
  - Avoid any
  - Avoid React.FC unless you want implicit children

- 2️⃣ Callback typing
  - Define callback signatures in props
  - Parent functions must conform automatically
  - Combine with useCallback only when identity matters

- 3️⃣ useState typing
  - Inference works for primitives
  - Explicit typing required for:
    - null
    - empty arrays/objects
    - unions

- 4️⃣ Event typing
  - `React.ChangeEvent<HTMLInputElement>`
  - Always type events
  - Never use `any`

- 5️⃣ useRef typing
  - DOM refs: useRef<T | null>
  - Mutable value refs: useRef<T>

- 6️⃣ Performance & hooks
  - useCallback stabilizes identity, not logic
  - Don’t memoize unless identity matters
  - Prefer functional updaters to avoid stale closures

- 7️⃣ Golden rules
  - Types describe intent, not implementation.
  - Stability matters more than allocation.
  - Inference is great—until it isn’t. 

### Session 5 useMemo, React.memo, and React Performance Myths

**Practical**
```tsx
function Dashboard({ trades }) {
  const totals = useMemo(
    () => calculateTotals(trades),
    [trades]
  );

  return (
    <>
      <Summary totals={totals} />
      <TradeList trades={trades} />
    </>
  );
}

```

- **What assumptions must be true for useMemo to be useful here?**
  - `Summary` is a memoized child
  - and `calculateTotals` is actually costly
  - renders happen frequently where trades identity often stays the same (or you’re trying to keep totals reference stable for memoized children)

- **Should Summary be memoized?**
  - Memoizing Summary only helps if Summary itself is non-trivial and its props are often referentially stable.
  - calculateTotals being costly is mainly an argument for useMemo, not React.memo(Summary).

- **Would memoizing TradeList help or hurt**
  - If trades is frequently recreated (new array each time) → React.memo(TradeList) is mostly useless (overhead + complexity).
  - If trades is stable most of the time (e.g., normalized store, selectors, RTK Query cache, or parent renders for unrelated reasons) → React.memo(TradeList) can help if TradeList is heavy.

- **What happens if trades is recreated but identical**
  - in this case both `Summary` and `TradeList` will be re-rendered
  - `const totals` will be re-rendered because dependency array updated;
  - `Summary` depends on `totals`

- **Insight**
  - if `trades` is often recreated , your real fix is upstream stability, not more memoizations
  - Avoid recreating `trades` unless data truly changed (selectors, memoized selectors, stable RTK query results, avoid map/filter inline in parent render)
  - Or compute `totals` closer to the data source (selector /backend/ query transform), so UI isn't doing heavy work per render. 

**Quizes**

- Q1 useMemo illusion
  ```tsx
  function App({ items }) {
    const count = useMemo(
      () => items.filter(i => i.active).length,
      [items]
    );

    return <div>{count}</div>;
  }

  ```
  - It prevents re-running the filter computation, not “recreating” the number (numbers are primitives).
  - it will save work when re-renders happen very often , but `items` reference stays the same; if `items` are huge, it will also save meaningful time (avoid O(N) scanning)
  - It depends whether `items` are big or not. Most of the time filtering can be trivial, and we usually just calculates count every render.

- Q2 “But my child is memoized!”

```tsx
const Child = React.memo(function Child({ value }) {
  console.log("Child render");
  return <div>{value}</div>;
});

function Parent() {
  const value = useMemo(() => 42, []);
  return <Child value={value} />;
}

```
  - Child only renders once 
  - not really, if Parent always pass 42 to Child, `React.memo` will also not re-render Child, seeing that 42 is identical to previous value.
  - Child does not re-render because `const value` is initialized once, and never updated.
  - **primitives don't need memoization**. `React.memo` already handles them perfectly.

- Q3 Function identity trap
  - Yes it does,
  - Because every render, a new `const onClick` is created
  - we should apply `useCallback` here with empty depenedency array; the click function is not a function that is going to change much. We can also do `useMemo` but return the function instead.
  - When we need the function to gets updated with every render, not just initialized once.

- Q4 useCallback dependency reality check
  -  No,
  -  This code is not correct because `user.id` is included in closure, and never gets updated.
  -  So the callback should be like this instead: `(id) => {saveUser(id)}`; `id` value should be injected by Child component. This bug happens because the `callback` is wrongly defined to contain a state (`user.id`) which is not static. 

- Q5 Memoization cascade (hard one)
  - TradeList
  - Summary
  - The real architecutre fix is to go up to the parent, make sure `trades` are not automatically recreated if there is no identity changes. So that downstream children can receive stable identity via props.

- Q6 Trick question: what’s actually expensive?
  A. Re-rendering a React component
  B. Running useMemo
  C. Allocating new objects/functions
  D. Updating the DOM

  D updating Dom
  - Dom mutation triggers layout, paint, compositing
  - Can block main thread
  - Orders of magnitude slower than JS
  
  - A(re-render) -> cheap
  - B(useMemo)  -> small overhead
  - C(allocations) -> matters in `hot path`, but still cheaper than DOM
  
  React render phase is cheap; browser is expensive

  
- Q7 Code review judgement
  -  I will challenge him about the `const value`, whether it is worth to `useMemo` for; I will aslo ask him what the time complexity is for `doThing` and question whether we need the `useCallback` or not; I will also question `React.memo`, about whether will the Child gets re-rendered anyway. 
  -  The smell i am looking for are unnecessary memoziation and comparison overhead brought by memoization.
  -  I think in this case this P.R is over-using memoizations

### Session 6 - Effects

**Mini-Practical**

```tsx
export function Profile({userId}) {
    const [user, setUser] = useState(null);
    useEffect(() => {
        fetchUser(userId).then(setUser);
    }, []);
}
```
Questions:

- **What’s wrong with this effect?**

This effects is only run once during initialization of Profile. Even though the effect relies on `userId`, its dependency array does not contain `userId`.
Also it did not define a proper type for user. 

- **What bug will appear?**

The `Profile` will re-render when given a new `userId`, but the `user` fetched will still be the very first `user`.

- **What should the dependency array be?**

`[userId]`

- **What happens in StrictMode?**

React is going to run the effect twice, and set the User twice.


**Quizes**

- Q1 - The “once on mount” lie
  ```tsx
  useEffect(() => {
    console.log("Hello");
  }, []);

  ```
  - 1. Because it has no dependencies, it will run once during creation 
  - 2. In strict mode, it will run more than once
  - 3. React is actually double checking whether your effect is idempotent, and safe to run more than once (without memory leaks etc)

- Q2 - Stale closure classic

  ```tsx
  function Counter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
      setInterval(() => {
        console.log(count);
      }, 1000);
    }, []);

    return <button onClick={() => setCount(c => c + 1)}>+</button>;
  }

  ```

  - 1. every 1 sec, 0 will be logged, forever.
  - 2. Becuase closure captures count at creation of `Counter`, which is 0.
  - 3. add `count` to dependency array; or we can do use `useRef` on count, and do `console.log(countRef.get())` instead.
  - 4. I prefer adding `count` to dependency array. 
  I think there is another bug here; `useEffect` in this case should return `clearInterval`; otherwise previous `Interval` will still be running; Not clearing the interval causes leaks and duplicated timers in StrictMode

- Q3 — Missing dependency (subtle) 

  ```ts
  function Profile({ userId }) {
    const [user, setUser] = useState(null);

    useEffect(() => {
      fetchUser(userId).then(setUser);
    }, []);
  }

  ```
  - 1. This effects is only run once during initialization of Profile. Even though the effect relies on `userId`, its dependency array does not contain `userId`.Also it did not define a proper type for user. 
  - 2. The `Profile` will re-render when given a new `userId`, but the `user` fetched will still be the very first `user`.
  - 3. It has nothing to do with React, closure is a javascript property. How it behaves is not controlled by react.  
  - 4. React will run the effect twice, and forces you to experience what non-idempotent effects do.

- Q4 — Effect vs render (very important)
  
  ```tsx
    const [total, setTotal] = useState(0);

    useEffect(() => {
      setTotal(items.reduce((a, b) => a + b.price, 0));
    }, [items]);

  ```
  - 1. not really. 
  - 2. i think people confuse derivation vs synchronization. Effect is for synchronization.
  - 3. `total = items.reduce((a, b) => a + b.price, 0)`
  - 4. derivation vs synchronization. Effect is for something that CANNOT be done during render (like fetching a remote property)

- Q5 — Infinite loop diagnosis

  ```tsx
    useEffect(() => {
      setQuery(q => q + "!");
    }, [query]);

  ```
  - 1. Because there is no stopping condition, `q` constantly gets updated
  - 2. If effects updated states, render will be kicked off again; effects and render goes hand in hand. 
  - 3. Effects may update state when the update is conditional or converges (fetch → set once, subscription sync, etc.)

- Q6 - Effects vs events

  ```tsx
  useEffect(() => {
    submitOrder(order);
  }, [order]);

  ```

  - 1. it is like side-effects used to synchronize states;
  - 2. Imagin a user submitting order without confirming? that is a hue problem; an action such as submitting order should be handled with a handler (like `onClick`) so that intention is loud and clear.
  - 3. Logic should be inside a dedicated function like `onClick`  

- Q7 - Dependency array truth test
  - 1. **The dependency array controls when an effect runs.** 
    - False, Dependency array controls which render an effect corresponds to, not timing.
  - 2. **You may omit dependencies if you “know they won’t change”.**
    - False, code smell
  - 3. **Every value read inside an effect must be listed.**
    - True, best practices
  - 4.  **`useEffect` is the right place to derive state from props.**
    - False, why not we just derive during render? isn't that more straight forward and readable.

- Q8 - The senior question (final boss)
  - An effect should exist only to synchronize React’s rendered output with the outside world.

---

## React Redux phase 3

Redux is event-sourcing with constraints

### 3.1 Redux without React

Redux reducers are replayable state transition functions.

**Quiz**
1. **Why exactly is Date.now() inside a reducer considered “impure”?**

because the result is not idempotent, every dispatch of `touch` could result in a different `lastUpdated` state, eventhough the external state never really changed.

2. **What’s the “Redux-correct” way to set lastUpdated? (describe in 1–2 lines)**

in this case we should compute `Date.now()` and pass it to `touch`; basically do dependency injection.

3. **If we replay actions from a log, what breaks when reducers are impure?**

The state re-created from those actions will be different everytime; and that is a problem for OMS, because before market open, we will have to replay events to recreate all existing orders and their state. If the function is not pure and deterministic, then the order state will be messed up.


---
## React, Javascripts Fundamentals
- `const` is like final for Java, but it is **not static**

- A React function is component is **just** a fucntion
  
  An App
  ```js
  function App() {
    const remaining = todos.filter(t => !t.done).length;
    return <div>{remaining}</div>;
  }

  ```

  **On every re-render**, React does 
  ```js
    App();
  ```

  and `remaining` gets re-calculated

  **React throws away everything and re-runs the function**





