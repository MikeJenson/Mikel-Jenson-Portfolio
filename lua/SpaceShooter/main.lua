	love.graphics.setDefaultFilter('nearest', 'nearest')
	enemy = {}
	enemies_controller = {}
	enemies_controller.enemies = {}
	enemies_controller.image = love.graphics.newImage('enemy.png')

	function checkCollisions(enemies, bullets)
		for i,e in ipairs(enemies) do
			for _,b in pairs(bullets) do
				if b.y <= e.y + e.height and b.x > e.x and b.x < e.x + e.width then
					table.remove(enemies, i)
				end	
			end
		end		
	end

function love.load()
	game_over = false
	game_win = false
	backgroundimage = love.graphics.newImage('background.png')
	player = {}
	player.x = 400
	player.y = 500
	player.bullets = {}
	player.cooldown = 20
	player.speed = 10
	player.image = love.graphics.newImage('player.png')
	--player.fire_sound = love.audio.newSource('laser.wav')
	player.fire = function()
		if player.cooldown <= 0 then
			player.cooldown = 20
	--love.audio.play(player.fire_sound) will remove comment once I get a '.wav' file to include
			bullet = {}
			bullet.x = player.x + 20
			bullet.y = player.y - 5
			table.insert(player.bullets, bullet)
		end
	end
	for i = 0, 9 do
		enemies_controller:spawnEnemy(i * 80, 0)
	end
end

function enemies_controller:spawnEnemy(x, y)
	enemy = {}
	enemy.x = x
	enemy.y = y
	enemy.width = 50
	enemy.height = 50
	enemy.bullets = {}
	enemy.cooldown = 20
	enemy.speed = .75
	table.insert(self.enemies, enemy)
end

function enemy:fire()
	if self.cooldown <= 0 then
		self.cooldown = 20
		bullet = {}
		bullet.x = self.x - 5
		bullet.y = sely.y - 55
		table.insert(self.bullets, bullet)
	end
end

	-- Update is run 60 times per second
function love.update(dt)
	-- Start cooldown (above) timer
	player.cooldown = player.cooldown -1
	-- Player movement
	if love.keyboard.isDown("right") then
		player.x = player.x + player.speed
	elseif love.keyboard.isDown("left") then
		player.x = player.x - player.speed
	end
	-- Player fire bullet
	if love.keyboard.isDown("space") then
		player.fire()
	end

	if #enemies_controller.enemies == 0 then
		game_win = true
	end

	for _,e in pairs(enemies_controller.enemies) do
		if e.y >= love.graphics.getHeight() then
			game_over = true
		end
		e.y = e.y + 1 * enemy.speed
	end

	-- Bullet movement and removal after they leave the screen
	for i,v in ipairs(player.bullets) do
		if v.y < -10 then
			table.remove(player.bullets, i)
		end
		v.y = v.y - 10
	end
	checkCollisions(enemies_controller.enemies, player.bullets)
end

function love.draw()
	if game_over then
		love.graphics.scale(10)
		love.graphics.print("Game Over!")
		return
	elseif game_win then
		love.graphics.scale(3)
		love.graphics.setColor(255, 255, 0)
		love.graphics.print("Thank you for saving the planet!")
		return
	end
	love.graphics.setColor(255, 255, 255)
	love.graphics.draw(backgroundimage)
	-- Draw player
	
	love.graphics.draw(player.image, player.x, player.y, 0, 5)

	for _,e in pairs(enemies_controller.enemies) do
		love.graphics.draw(enemies_controller.image, e.x, e.y, 0, 5)
	end

	-- Draw bullet
	love.graphics.setColor(0, 255, 50)
	for _,v in pairs(player.bullets) do
		love.graphics.rectangle("fill", v.x, v.y, 10, 10)
	end
end