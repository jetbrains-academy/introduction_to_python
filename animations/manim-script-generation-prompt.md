# Manim Script Generation Prompt for Programming Concept Animations

## Objective
Generate a complete, **standalone** Manim script for a **30-second educational animation** that explains a programming concept using metaphors and visual storytelling. The animation must include JetBrains branding (intro and outro) and follow established patterns for consistency and quality.

**Key Requirements:**
- Standalone script with no external dependencies (except JetBrains logo)
- Use only Manim primitives - no SVG assets or AI_Metaphors imports
- Include color constants as class variables
- Configurable logo path via class constant

---

## Animation Structure

Every animation follows this **three-part structure**:

1. **Intro (3-4 seconds)**: Display concept title with JetBrains logo
2. **Body (22-24 seconds)**: Main content - 3-5 scenes explaining the concept
3. **Outro (3-4 seconds)**: Display "Thanks for watching!" with JetBrains logo

**Total Duration**: ~30 seconds

---

## Required Components

### 1. Imports and Setup

```python
from manim import *

# For voice animations, also include:
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
```

**Note**: The scripts are now standalone and only require the JetBrains logo file. No AI_Metaphors dependencies needed.

### 2. Scene Class Structure

**Basic Animation Template:**
```python
class ConceptName(Scene):
    """
    Educational animation explaining [Concept Name].
    Duration: ~30 seconds

    Standalone version - only requires JetBrains logo.
    """

    # Configure logo path (can be overridden)
    LOGO_PATH = "animations/JetBrains-logo.png"

    # JetBrains color palette
    TEAL = "#28b8a0"
    ORANGE = "#fc801d"
    PINK = "#ff318c"
    PURPLE = "#6b57ff"

    def construct(self):
        # INTRO: Display concept title with JetBrains logo
        self.intro_screen("Concept Name")

        # BODY: Main animation content (3-5 scenes)
        self.scene1()
        self.scene2()
        self.scene3()
        # ... additional scenes as needed

        # OUTRO: Thank you with JetBrains logo
        self.outro_screen()

    def remove_everything(self):
        """Remove all objects from the scene."""
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

    def intro_screen(self, concept_title: str):
        """Display concept title with JetBrains logo (intro screen)."""
        self.remove_everything()

        # Create title text
        title_text = Text(concept_title, color=WHITE, font_size=48, weight=BOLD)

        # Create and position logo
        logo = ImageMobject(self.LOGO_PATH).scale(0.3)
        logo.next_to(title_text, DOWN, buff=0.5)

        # Animate title and logo
        self.play(Write(title_text), run_time=1)
        self.play(FadeIn(logo), run_time=0.5)
        self.wait(2)

        # Clear screen for transition to body
        self.remove_everything()

    def outro_screen(self):
        """Display thank you message with JetBrains logo (outro screen)."""
        self.remove_everything()

        # Create thank you text
        thank_you = Text("Thanks for watching!", color=WHITE, font_size=40)

        # Create and position logo
        logo = ImageMobject(self.LOGO_PATH).scale(0.3)
        logo.next_to(thank_you, DOWN, buff=0.5)

        # Animate text and logo
        self.play(Write(thank_you), run_time=1)
        self.play(FadeIn(logo), run_time=0.5)
        self.wait(2)

        # Clear screen
        self.remove_everything()

    def describe_scene(self, caption: str):
        """Display brief explanatory text at top of screen."""
        text = Text(caption, font_size=24, color=WHITE).to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

    def scene1(self):
        """First scene of the animation."""
        # Scene implementation
        pass

    # Additional scene methods...
```

**Voice Animation Template:**
```python
class ConceptName(VoiceoverScene):
    """
    Educational animation with voiceover explaining [Concept Name].
    Duration: ~30 seconds

    Standalone version - only requires JetBrains logo.
    """

    # Configure logo path (can be overridden)
    LOGO_PATH = "animations/JetBrains-logo.png"

    # JetBrains color palette
    TEAL = "#28b8a0"
    ORANGE = "#fc801d"
    PINK = "#ff318c"
    PURPLE = "#6b57ff"

    def construct(self):
        # Set up voice service
        self.set_speech_service(OpenAIService(voice="onyx"))

        # INTRO: Display concept title with JetBrains logo
        self.intro_screen("Concept Name")

        # BODY: Use narrate() to sync voice with animations
        self.narrate("<explain>Let's understand this concept.</explain>", self.scene1)
        self.narrate("<happy>Here's how it works!</happy>", self.scene2)

        # OUTRO: Thank you with JetBrains logo
        self.outro_screen()

    def narrate(self, text: str, builder):
        """Narrate text while executing builder function."""
        with self.voiceover(text=text) as tracker:
            builder(self)

    # Include remove_everything, intro_screen, outro_screen, describe_scene as above

    def scene1(self, scene):
        """Scene builder function."""
        # Animation code
        pass
```

---

## JetBrains Branding Requirements

### Color Palette (MANDATORY)

**Use ONLY these colors** (defined as class constants):

```python
# JetBrains color palette (define these as class constants)
TEAL = "#28b8a0"      # Primary accent
ORANGE = "#fc801d"     # Secondary accent
PINK = "#ff318c"       # Highlight
PURPLE = "#6b57ff"     # Emphasis
# WHITE and BLACK are Manim defaults
```

**Color Usage Guidelines:**
- **Background**: Always black (Manim default)
- **Primary text**: White (Manim WHITE constant)
- **Main objects**: Teal (`self.TEAL`)
- **Accents**: Orange, Pink, Purple for variety
- **Avoid**: Any colors outside this palette
- **Reference colors**: Use `self.TEAL`, `self.ORANGE`, `self.PINK`, `self.PURPLE` in your code

### Logo Integration

**Logo File**: Configurable via `LOGO_PATH` class constant (default: `"animations/JetBrains-logo.png"`)

**Intro Screen** (`intro_screen()` method):
- Display concept title in large, bold font (48pt, white)
- JetBrains logo below title, scaled to 0.3, with 0.5 buffer
- Animate title write (1 second), then logo fade-in (0.5 seconds)
- Wait 2 seconds before clearing and transitioning to body

**Outro Screen** (`outro_screen()` method):
- Display "Thanks for watching!" (40pt font, white)
- JetBrains logo below text, scaled to 0.3, with 0.5 buffer
- Animate text write (1 second), then logo fade-in (0.5 seconds)
- Wait 2 seconds before clearing

---

## Animation Best Practices

### Timing Guidelines

- **Intro/Outro**: 2 seconds each
- **Scene Transitions**: 0.5 seconds fade
- **Between Scenes**: 1-2 seconds wait
- **Per Scene**: 4-8 seconds (aim for 5-6)
- **Total Body**: 22-24 seconds for 3-5 scenes

### Composition Rules

1. **Text Limits**:
    - Maximum 3 text elements on screen simultaneously
    - Keep sentences short (under 10 words)
    - Font sizes: 24-40pt (titles), 18-24pt (body)

2. **Object Positioning**:
    - Use `.to_edge(UP/DOWN/LEFT/RIGHT)` for screen edges
    - Use `.to_corner(UL/UR/DL/DR)` for corners
    - Use `.next_to(obj, direction)` for relative positioning
    - Avoid overlapping objects
    - Keep objects within frame bounds

3. **Scene Clearing**:
    - Call `self.remove_everything()` between major scene changes
    - Or use selective `FadeOut` for specific objects

4. **Animation Types**:
    - **Create**: For drawing paths, shapes
    - **Write**: For text appearance
    - **FadeIn/FadeOut**: For smooth transitions
    - **Transform**: For morphing objects
    - **MoveToTarget**: For position changes
    - **AnimationGroup**: For simultaneous animations

### Visual Design Patterns

**Pattern 1: Progressive Build-Up**
```python
def scene1(self):
    # Introduce elements one by one
    title = Text("Step 1", font_size=30, color=WHITE).to_edge(UP)
    self.play(Write(title))

    obj1 = Circle(radius=1, color=self.TEAL).shift(LEFT * 2)
    self.play(Create(obj1))
    self.wait(1)

    obj2 = Square(side_length=1.5, color=self.ORANGE).shift(RIGHT * 2)
    self.play(Create(obj2))
    self.wait(1)

    # Clean up
    self.play(FadeOut(title), FadeOut(obj1), FadeOut(obj2))
```

**Pattern 2: Step-by-Step Transformation**
```python
def scene2(self):
    # Show transformation process
    start = Text("Input", color=self.TEAL)
    self.play(Write(start))
    self.wait(1)

    arrow = Arrow(LEFT, RIGHT, color=WHITE)
    end = Text("Output", color=self.ORANGE)

    self.play(Transform(start, arrow))
    self.wait(0.5)
    self.play(Transform(start, end))
    self.wait(1)
```

**Pattern 3: Metaphor Visualization**
```python
def scene3(self):
    # Use Manim primitives for metaphors
    container = Rectangle(width=4, height=3, color=self.PURPLE)
    items = VGroup(*[Circle(radius=0.2, color=self.ORANGE) for _ in range(5)])
    items.arrange(RIGHT, buff=0.3).move_to(container)

    self.play(Create(container))
    self.play(LaggedStart(*[FadeIn(item) for item in items], lag_ratio=0.2))
    self.wait(2)
```

---

## Creating Custom Shapes and Objects

**Use Manim primitives** to create all visual elements (standalone, no external dependencies):

### Available Manim Shapes

**Basic Shapes:**
- `Circle(radius=1, color=self.TEAL)` - Circle
- `Square(side_length=2, color=self.ORANGE)` - Square
- `Rectangle(width=3, height=2, color=self.PURPLE)` - Rectangle
- `RoundedRectangle(width=3, height=2, corner_radius=0.2, color=self.TEAL)` - Rounded rectangle
- `Triangle(color=self.PINK)` - Triangle
- `RegularPolygon(n=6, color=self.PURPLE)` - Polygon with n sides
- `Star(n=5, color=self.ORANGE)` - Star with n points

**Lines and Arrows:**
- `Arrow(start, end, color=WHITE)` - Arrow from start to end
- `Line(start, end, color=WHITE)` - Line
- `Dot(point, color=self.TEAL)` - Small dot/point
- `DashedLine(start, end, color=WHITE)` - Dashed line

**Text and Math:**
- `Text("Hello", font_size=32, color=WHITE)` - Text
- `MathTex(r"\sum_{i=1}^{n} x_i", color=WHITE)` - LaTeX math
- `Code(code="print('hello')", language="python")` - Code block

**Grouping:**
- `VGroup(obj1, obj2, obj3)` - Group objects vertically
- `VGroup().arrange(RIGHT, buff=0.5)` - Arrange objects

### Example: Creating Complex Shapes with Helper Methods

Instead of using external SVG files, create helper methods for custom shapes:

```python
def create_tag(self, scale=1.0, color=None):
    """Create a tag/label shape using Manim primitives."""
    if color is None:
        color = self.TEAL

    # Create a rounded rectangle for the tag body
    tag_body = RoundedRectangle(
        width=2.0 * scale,
        height=1.2 * scale,
        corner_radius=0.2 * scale,
        color=color,
        stroke_width=3
    )

    # Create a small circle for the tag hole
    tag_hole = Circle(
        radius=0.15 * scale,
        color=color,
        fill_opacity=0,
        stroke_width=3
    )
    tag_hole.move_to(tag_body.get_left() + RIGHT * 0.3 * scale)

    # Group them together
    tag = VGroup(tag_body, tag_hole)
    return tag

# Usage
tag = self.create_tag(scale=1.2, color=self.TEAL)
tag.shift(LEFT * 2)
self.play(FadeIn(tag))
```

### Example: Creating a Book Shape

```python
def create_book(self, scale=1.0, color=None):
    """Create a simple book shape using rectangles."""
    if color is None:
        color = self.PURPLE

    # Book cover
    cover = RoundedRectangle(
        width=1.5 * scale,
        height=2.0 * scale,
        corner_radius=0.1 * scale,
        color=color,
        fill_opacity=0.3,
        stroke_width=3
    )

    # Book spine lines
    line1 = Line(
        cover.get_top() + DOWN * 0.3 * scale,
        cover.get_bottom() + UP * 0.3 * scale,
        color=color,
        stroke_width=2
    ).shift(LEFT * 0.4 * scale)

    line2 = Line(
        cover.get_top() + DOWN * 0.3 * scale,
        cover.get_bottom() + UP * 0.3 * scale,
        color=color,
        stroke_width=2
    ).shift(LEFT * 0.2 * scale)

    book = VGroup(cover, line1, line2)
    return book
```

**Benefits of Manim Primitives:**
- ✅ Standalone - no external file dependencies
- ✅ Customizable - easily adjust size, color, proportions
- ✅ Reusable - create helper methods for common shapes
- ✅ Consistent - works across all environments

---

## Code Quality Requirements

### Structure
- **Clear scene separation**: Each scene in its own method
- **Descriptive names**: `scene1_introduction`, `scene2_transformation`, etc.
- **Helper methods**: Reuse `remove_everything()`, `start_end_scene()`, `describe_scene()`
- **Comments**: Brief comments explaining each scene's purpose

### Avoid Common Pitfalls
- **Overlapping objects**: Use explicit positioning
- **Off-screen objects**: Check bounds with `.get_center()`, `.get_edge_center()`
- **Too much text**: Maximum 3 text objects, short sentences
- **Missing waits**: Add `self.wait()` between major actions
- **Color violations**: Only use JetBrains palette colors
- **Timing issues**: Test that total duration is ~30 seconds

### Error Prevention
- Import all required Manim classes
- Use correct file paths for logo and SVGs
- Handle edge cases (empty lists, None values)
- Test positioning before finalizing

---

## Example: Complete Animation Script

```python
from manim import *

class VariableAssignment(Scene):
    """
    Explains variable assignment using a box-and-label metaphor.
    Duration: ~30 seconds

    Standalone version - only requires JetBrains logo.
    """

    # Configure logo path (can be overridden)
    LOGO_PATH = "animations/JetBrains-logo.png"

    # JetBrains color palette
    TEAL = "#28b8a0"
    ORANGE = "#fc801d"
    PINK = "#ff318c"
    PURPLE = "#6b57ff"

    def construct(self):
        # INTRO: Display concept title with JetBrains logo
        self.intro_screen("Variable Assignment")

        # BODY: Main animation content
        self.scene1_introduce_box()
        self.scene2_assign_value()
        self.scene3_update_value()
        self.scene4_conclusion()

        # OUTRO: Thank you with JetBrains logo
        self.outro_screen()

    def remove_everything(self):
        """Remove all objects from the scene."""
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)

    def intro_screen(self, concept_title: str):
        """Display concept title with JetBrains logo (intro screen)."""
        self.remove_everything()

        # Create title text
        title_text = Text(concept_title, color=WHITE, font_size=48, weight=BOLD)

        # Create and position logo
        logo = ImageMobject(self.LOGO_PATH).scale(0.3)
        logo.next_to(title_text, DOWN, buff=0.5)

        # Animate title and logo
        self.play(Write(title_text), run_time=1)
        self.play(FadeIn(logo), run_time=0.5)
        self.wait(2)

        # Clear screen for transition to body
        self.remove_everything()

    def outro_screen(self):
        """Display thank you message with JetBrains logo (outro screen)."""
        self.remove_everything()

        # Create thank you text
        thank_you = Text("Thanks for watching!", color=WHITE, font_size=40)

        # Create and position logo
        logo = ImageMobject(self.LOGO_PATH).scale(0.3)
        logo.next_to(thank_you, DOWN, buff=0.5)

        # Animate text and logo
        self.play(Write(thank_you), run_time=1)
        self.play(FadeIn(logo), run_time=0.5)
        self.wait(2)

        # Clear screen
        self.remove_everything()

    def describe_scene(self, caption: str):
        """Display brief explanatory text at top of screen."""
        text = Text(caption, font_size=24, color=WHITE).to_edge(UP)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

    def scene1_introduce_box(self):
        """Introduce the box metaphor for variables."""
        # Show empty box with label
        box = Rectangle(width=2.5, height=2, color=self.TEAL, stroke_width=4)
        label = Text("x", font_size=36, color=WHITE).next_to(box, UP)

        self.play(Create(box))
        self.play(Write(label))
        self.wait(2)

        # Keep for next scene
        self.box = box
        self.label = label

    def scene2_assign_value(self):
        """Demonstrate assigning a value to the variable."""
        # Show code
        code = Text("x = 5", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(code))
        self.wait(1)

        # Put value in box
        value = Text("5", font_size=48, color=self.ORANGE).move_to(self.box)
        self.play(FadeIn(value))
        self.wait(2)

        self.play(FadeOut(code))
        self.value = value

    def scene3_update_value(self):
        """Show updating the variable with a new value."""
        # Show new assignment
        code = Text("x = 10", font_size=32, color=WHITE).to_edge(UP)
        self.play(Write(code))
        self.wait(1)

        # Replace old value
        new_value = Text("10", font_size=48, color=self.PINK).move_to(self.box)
        self.play(Transform(self.value, new_value))
        self.wait(2)

        self.play(FadeOut(code))

    def scene4_conclusion(self):
        """Summarize the concept."""
        summary = Text(
            "Variables store and update values",
            font_size=28,
            color=WHITE
        ).to_edge(DOWN)

        self.play(Write(summary))
        self.wait(2)

        # Clean up
        self.remove_everything()
```

---

## Voice Animation Specifics

If creating a **voice-enabled animation**, follow these additional guidelines:

### Emotion Tags
Use emotion tags to control voice tone:
- `<explain>`: Explanatory, educational tone
- `<happy>`: Enthusiastic, positive tone
- `<curious>`: Questioning, wondering tone
- `<emphasis>`: Strong emphasis on key points

**Example:**
```python
self.narrate("<explain>Let's see how variables work.</explain>", self.scene1)
self.narrate("<happy>Now we can store our value!</happy>", self.scene2)
```

### Scene Builder Pattern
```python
def scene1(self, scene):
    """Scene builder receives scene reference."""
    box = Rectangle(width=2, height=2, color="#28b8a0")
    scene.play(Create(box))
    scene.wait(1)
```

### Narration Sync
- Keep narration concise (1-2 sentences per scene)
- Match animation complexity to narration length
- Use `scene.wait()` to extend timing if needed

---

## Generation Checklist

Before finalizing your Manim script, verify:

- [ ] **Structure**: Intro → Body (3-5 scenes) → Outro
- [ ] **JetBrains Intro**: Concept title + logo using `intro_screen()` (3-4 seconds)
- [ ] **JetBrains Outro**: "Thanks for watching!" + logo using `outro_screen()` (3-4 seconds)
- [ ] **Color Constants**: TEAL, ORANGE, PINK, PURPLE defined as class constants
- [ ] **Color Palette**: Only JetBrains colors used (self.TEAL, self.ORANGE, etc.)
- [ ] **Logo Path**: LOGO_PATH class constant defined
- [ ] **Duration**: Total ~30 seconds (22-24s for body)
- [ ] **Scene Separation**: Each scene in its own method
- [ ] **Positioning**: All objects within frame, no overlaps
- [ ] **Text Limits**: Max 3 text elements, short sentences
- [ ] **Timing**: Appropriate waits between actions
- [ ] **Helper Methods**: `remove_everything()`, `intro_screen()`, `outro_screen()`, `describe_scene()` included
- [ ] **Imports**: Only `from manim import *` (no AI_Metaphors dependencies)
- [ ] **Standalone**: No external dependencies except JetBrains logo
- [ ] **Comments**: Brief explanations for each scene
- [ ] **Metaphor**: Clear visual metaphor for programming concept
- [ ] **Clarity**: Animation teaches concept effectively

---

## Input Format

When generating a script, you'll receive:

**Required:**
- **Concept Name**: The programming term/concept to explain (e.g., "Variable Assignment", "For Loop")
- **Concept Definition/Description**: What the concept means
- **Target Duration**: ~30 seconds

**Optional:**
- **Preferred Metaphor**: Suggested visual metaphor
- **Animation Type**: Basic or Voice
- **Logo Path**: Custom path to JetBrains logo (if different from default)

---

## Output Format

Provide:
1. **Complete Python Script**: Ready to execute with Manim (standalone, no external dependencies except logo)
2. **Concept Title**: For the intro screen (e.g., "Variable Assignment")
3. **Scene Breakdown**: Brief description of each scene (1-2 sentences)
4. **Estimated Duration**: Total and per-scene timing

**Example Output:**

```
Concept Title: "Variable Assignment"

Scene Breakdown:
- Intro (3.5s): Display "Variable Assignment" title with JetBrains logo
- Scene 1 (5s): Introduce empty box with label "x"
- Scene 2 (6s): Assign value "5" to variable, show it entering the box
- Scene 3 (6s): Update variable to "10", replace old value
- Scene 4 (5s): Display summary text
- Outro (3.5s): Display "Thanks for watching!" with JetBrains logo

Estimated Duration: 29 seconds

[Python script follows...]
```

---

## Final Notes

- **Standalone scripts**: No AI_Metaphors dependencies - only JetBrains logo required
- **Focus on clarity**: The animation should teach effectively
- **Visual storytelling**: Use metaphors that resonate
- **Brand consistency**: JetBrains colors and logo throughout
- **Timing precision**: Test that duration matches target
- **Code quality**: Clean, commented, maintainable code
- **Reusability**: Helper methods for common operations and custom shapes
- **Portability**: Scripts should run on any system with Manim installed

**Remember**: The goal is to create an engaging, educational 30-second animation that explains a programming concept through visual metaphor while maintaining JetBrains brand identity. All scripts should be self-contained and portable, using only Manim primitives and the JetBrains logo.

Good luck with your animation generation!
