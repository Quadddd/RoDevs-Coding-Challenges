local s = tostring
local function f(n, t)
	n = s(n)
	t = s(t)
	local x = {}
	for i, v in pairs(n:split('')) do
		table.insert(x, v == t and i or nil)
	end
end
